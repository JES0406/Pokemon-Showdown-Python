'''
Module for the battle system of the game.

The battle system is turn-based and consists of two players, each with a team of N Pokemon. 
Where N ∈ [1, 6].
The players take turns to select a move for their Pokemon to use. The move is then executed and the effects are applied.
'''

from Code.DataStructures.Pokemon import Pokemon
from Code.DataStructures.Move import Move
from Code.DataStructures.Player import Player
from Code.exceptions import ReturnBackException
from Code.DataStructures.MoveExecution import MoveExecution
import random
import time

class Battle:
    def __init__(self, players: list[Player] = [], id: int = 0):
        self._players = players
        self._turn = 0
        self._current_turn_order = []
        self._winner = None
        self._weather = None
        self._terrain = None
        self._move_execution = MoveExecution()
        self._id = id
        self._time = time.time()
        self._date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(self._time))

    # Setters and getters
    @property
    def id(self):
        return self._id
    
    @property
    def players(self):
        return self._players
    
    @property
    def turn(self):
        return self._turn
    
    @property
    def current_turn_order(self):
        return self._current_turn_order   
        
    @property
    def winner(self):
        return self._winner
    
    @property
    def weather(self):
        return self._weather
    
    @property
    def terrain(self):
        return self._terrain
    
    @property
    def move_execution(self):
        return self._move_execution
    
    # Methods
    def turn_order(self, move1: Move, move2: Move): # Currently only for 2 players
        if move1.priority > move2.priority:
            self._current_turn_order = [0, 1]
        elif move1.priority < move2.priority:
            self._current_turn_order = [1, 0]
        else:
            speed1 = self._players[0].current_pokemon.stats['spe']*self._players[0].current_pokemon.get_boost('spe')
            speed2 = self._players[1].current_pokemon.stats['spe']*self._players[1].current_pokemon.get_boost('spe')
            if speed1 == speed2:
                self._current_turn_order = [0, 1] if random.randint(0, 1) == 0 else [1, 0]  # Randomize turn order
            elif speed1 > speed2:
                self._current_turn_order = [0, 1]
            else:
                self._current_turn_order = [1, 0]


    def is_finished(self):
        for player in self._players:
            if all(pokemon.status == 'FNT' for pokemon in player.team):
                finished = True
                break
        else:
            finished = False

        return finished
            
    
    def calculate_damage(self, move: Move, attacker: Pokemon, defender: Pokemon):
        base_power = 0

        # Handle Status moves
        if move.category == 'Status':
            move.use()  # Apply the effects of the Status move
            return 0  # Status moves typically don't deal damage

        # Get the base power from the move
        try:
            base_power = move.use()  # Ensure move.use() is properly called for the base power
        except ValueError as e:
            print(e)
            return 0  # Return 0 if there's an error

        # Calculate critical hit chance
        crit = random.randint(1, 24) == 1  # Critical hit on a roll of 1

        # Calculate attack and defense based on move category
        if move.category == 'Physical':
            attack = attacker.stats['atk'] * attacker.get_boost('atk')
            defense = defender.stats['def'] if crit else defender.stats['def'] * defender.get_boost('def')
        elif move.category == 'Special':
            attack = attacker.stats['spa'] * attacker.get_boost('spa')
            defense = defender.stats['spd'] if crit else defender.stats['spd'] * defender.get_boost('spd')
        else:
            return 0  # If the move category is invalid, return 0

        # Calculate damage
        damage = (((2 * attacker.level / 5 + 2) * base_power * attack / defense) / 50 + 2)

        return damage

    
    def apply_damage(self, move: Move, attacker: Pokemon, defender: Pokemon, damage: float): # Add glaive rush mechanic
        damage = damage*100/defender.stats['hp']
        if move.type == defender.types[0] or move.type == defender.types[1]:
            damage = damage * 1.5
        if self._weather != None:
            damage = self.apply_weather_effects(move, damage)
        
        damage *= random.uniform(0.85, 1.0)
        # Type effectiveness (to be implemented)
        if move.category == 'Physical' and attacker.status == 'BRN':
            damage = damage * 0.5

        defender.current_hp = -round(damage, 0)

    def apply_weather_effects(self, move, damage):
        if self._weather == 'Rain':
            if move.type == 'Water':
                return damage * 1.5
            elif move.type == 'Fire':
                return damage * 0.5
        elif self._weather == 'Sun':
            if move.type == 'Fire':
                return damage * 1.5
            elif move.type == 'Water':
                return damage * 0.5
        return damage

    def apply_effects(self, move: Move, attacker: Pokemon, defender: Pokemon):
        # To be implemented
        pass

    def get_info(self, player: Player):
        # Get information about the current player's Pokemon
        print(player.current_pokemon)
        for i, move in enumerate(player.current_pokemon.moves):
            print(f"{i+1}. {move}")

    def move_logic(self, player: Player):
        while 1:
            move_index = int(input(f"Player {player.name}, choose a move (0-{len(player.current_pokemon.moves)-1}), or -1 to cancel: "))
            try:
                if move_index == -1:
                    raise ReturnBackException("Move cancelled")
                player.move = move_index  # Set the move using the player's setter
                return player.move
            except ValueError as e:
                print(e)

    def switch_logic(self, player: Player):
        while 1:
            pokemon_index = int(input(f"Player {player.name}, choose a Pokemon to switch to (0-{len(player.team)-1}), or -1 to cancel: "))
            try:
                if pokemon_index == -1:
                    raise ReturnBackException("Switch cancelled")
                player.switch_pokemon(pokemon_index)  # Switch to the chosen Pokemon
            except ValueError as e:
                print(e)

    def order_input(self, player: Player):
        order = 3
        while order == 3:
            try:
                player.switch = False
                order = input(f"""Player {player.name}, choose:\n1. Move\n2. Switch Pokemon\n3. Get Info\n""")
                if order == "1":
                    self.move_logic(player)
                elif order == "2":
                    self.switch_logic(player)
                elif order == "3":
                    self.get_info(player)
                else:
                    print("Invalid input. Please try again.")
            except ReturnBackException as e:
                print(e)
                order = 3
            order = int(order)

    def run(self, testing=False):
        while self.winner is None:
            # Get and validate moves for both players
            for player in self._players:
                print(f"Player {player.name}'s turn!")
                self.order_input(player)

            # Determine the turn order based on the moves
            players = [0, 1]
            for i, player in enumerate(self._players):
                if player.switch:
                    players.remove(i)
            if len(players) == 2:
                self.turn_order(self._players[0].move, self._players[1].move)
            else:
                self._current_turn_order = players

            # Execute moves in the determined turn order
            for i in self._current_turn_order:
                attacker = self._players[i]
                defender = self._players[1 - i]

                move = attacker.move  # The chosen move for the current player
                if not testing:
                    print(f"Player {i+1}'s {attacker.current_pokemon.name} uses {move.name}!")
                
                # Calculate and apply damage
                damage = self.move_execution.calculate_damage(move, attacker.current_pokemon, defender.current_pokemon)
                damage = self.move_execution.apply_damage(move, attacker.current_pokemon, defender.current_pokemon, damage, self._weather)
                if not testing:
                    print(f"It deals {damage} damage!")

                # Apply any additional effects (status, etc.)
                self.apply_effects(move, attacker.current_pokemon, defender.current_pokemon)

                if not testing:
                    print(f"Player {1-i+1}'s {defender.current_pokemon.name} has {defender.current_pokemon.current_hp} HP remaining!")

                # Check if the battle is finished
                if self.is_finished():
                    self._winner = attacker
                    break
            self._turn += 1

        else:
            if not testing:
                print(f"Player {self._players.index(self._winner) + 1} wins!")


    def __str__(self):
        return f"Battle between {self._players[0].name} and {self._players[1].name}"
    
    def __repr__(self):
        return f"{self.id}, {self._players[0].id}, {self._players[1].id}, {self._winner.id}, {self._date}"

