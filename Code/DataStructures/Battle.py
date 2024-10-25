'''
Module for the battle system of the game.

The battle system is turn-based and consists of two players, each with a team of N Pokemon. 
Where N ∈ [1, 6].
The players take turns to select a move for their Pokemon to use. The move is then executed and the effects are applied.
'''

from Code.DataStructures.Pokemon import Pokemon
from Code.DataStructures.Move import Move
from Code.DataStructures.Player import Player
from Code.exceptions import ReturnBackException, NoPPException
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

    def get_info(self, player: Player):
        # Get information about the current player's Pokemon
        print(player.current_pokemon)
        for i, move in enumerate(player.current_pokemon.moves):
            print(f"{i+1}. {move}")

    def move_logic(self, player: Player):
        while 1:
            move_index = int(input(f"Player {player.name}, choose a move (1-{len(player.current_pokemon.moves)}), or -1 to cancel: "))
            try:
                if move_index == -1:
                    raise ReturnBackException("Move cancelled")
                player.move = move_index - 1  # Set the move using the player's setter. The index is 1-based for the user so we need to subtract 1
                if player.move.pp == 0:
                    raise ReturnBackException("No PP left for this move!")
                return player.move
            except ValueError as e:
                print(e)

    def switch_logic(self, player: Player):
        while 1:
            pokemon_index = int(input(f"Player {player.name}, choose a Pokemon to switch to (1-{len(player.team)}), or -1 to cancel: "))
            try:
                if pokemon_index == -1:
                    raise ReturnBackException("Switch cancelled")
                player.switch_pokemon(pokemon_index - 1)  # Switch to the chosen Pokemon. The index is 1-based for the user so we need to subtract 1
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
                damage = self.move_execution.apply_damage(move, attacker.current_pokemon, defender.current_pokemon, self._weather)
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

