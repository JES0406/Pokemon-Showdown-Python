'''
Module for the battle system of the game.

The battle system is turn-based and consists of two players, each with a team of N Pokemon. 
Where N ∈ [1, 6].
The players take turns to select a move for their Pokemon to use. The move is then executed and the effects are applied.
'''

from Code.pokemon import Pokemon
from Code.move import Move
from Code.player import Player
import random

class Battle:
    def __init__(self, players: list[Player]):
        self._players = players
        self._turn = 0
        self._current_turn_order = []
        self._winner = None
        self._weather = None
        self._terrain = None

    # Setters and getters
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
    
    # Methods
    def turn_order(self, move1: Move, move2: Move): # Currently only for 2 players
        if move1.priority > move2.priority:
            self._current_turn_order = [self._players[0], self._players[1]]
        elif move1.priority < move2.priority:
            self._current_turn_order = [self._players[1], self._players[0]]
        else:
            speed1 = self._players[0].current_pokemon.stats['spe']*self._players[0].current_pokemon.get_boost('spe')
            speed2 = self._players[1].current_pokemon.stats['spe']*self._players[1].current_pokemon.get_boost('spe')
            if speed1 == speed2:
                self._current_turn_order = [[0,1], [1,0]][random.randint(0,1)]
            self._current_turn_order = [speed1>speed2, speed2>speed1]


    def is_finished(self):
        for player in self._players:
            if all(pokemon.status == 'FNT' for pokemon in player.team):
                finished = True
                break
        else:
            finished = False

        return finished
      
    def execute_move(self, move_index: int):
        base_power = 0
        moves = self._players[self._current_turn_order[self._turn]].current_pokemon.moves
        if move_index >= len(moves):
            raise ValueError("Move index out of range")
        move = moves[move_index]
        if move.category == 'Status':
            move.use()
        try:
            base_power = moves[move_index].use()
        except ValueError as e:
            print(e)
        return base_power
    
    def calculate_damage(self, move: Move, attacker: Pokemon, defender: Pokemon):
        crit_result = random.randint(1, 24)
        if crit_result == 1:
            crit = True
        else:
            crit = False
        if move.category == 'Physical':
            attack = attacker.stats['atk']*attacker.get_boost('atk')
            if crit:
                defense = defender.stats['def']
            else:
                defense = defender.stats['def']*defender.get_boost('def')
        elif move.category == 'Special':
            attack = attacker.stats['spa']*attacker.get_boost('spa')
            if crit:
                defense = defender.stats['spd']
            else:
                defense = defender.stats['spd']*defender.get_boost('spd')
        else:
            return 0
        damage = (((2 * attacker.level / 5 + 2) * move.power * attack / defense) / 50 + 2)
        return damage
    
    def apply_damage(self, move: Move, attacker: Pokemon, defender: Pokemon, damage: float): # Add glaive rush mechanic
        damage = damage*100/defender.stats['hp']
        if move.type == defender.type:
            damage = damage * 1.5
        if self._weather != None:
            if self._weather == 'Rain':
                if self.move.type == 'Water':
                    damage = damage * 1.5
                elif self.move.type == 'Fire':
                    damage = damage * 0.5
            elif self._weather == 'Sun':
                if self.move.type == 'Fire':
                    damage = damage * 1.5
                elif self.move.type == 'Water':
                    damage = damage * 0.5
        
        damage *= random.uniform(0.85, 1.0)
        # Type effectiveness (to be implemented)
        if move.category == 'Physical' and attacker.status == 'BRN':
            damage = damage * 0.5

        defender.current_hp = -round(damage, 0)

    def apply_effects(self, move: Move, attacker: Pokemon, defender: Pokemon):
        # To be implemented
        pass

    def switch_pokemon(self, player: Player, pokemon_index: int):
        player.current_pokemon = pokemon_index

    def run(self):
        # To be implemented
        pass        