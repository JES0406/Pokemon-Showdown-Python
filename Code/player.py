'''
module for player class

The player class is used to represent a player in the game.
The player has attributes such as name, team, and current pokemon and terastization, mega evolution and dynamaaxing flags.
'''

from Code.pokemon import Pokemon
from Code.move import Move

class Player:
    def __init__(self, name: str, team: list[Pokemon]):
        self._name = name
        self._team = team
        self._current_pokemon = 0
        self._terastization = False
        self._mega_evolution = False
        self._dynamaaxing = False

    # Setters and getters
    @property
    def name(self):
        return self._name
    
    @property
    def team(self):
        return self._team
    
    @property
    def current_pokemon(self):
        return self._team[self._current_pokemon]
    
    @current_pokemon.setter
    def current_pokemon(self, pokemon_index):
        self._current_pokemon = pokemon_index
    
    @property
    def terastization(self):
        return self._terastization
    
    @terastization.setter
    def terastization(self, terastization):
        self._terastization = terastization
    
    @property
    def mega_evolution(self):
        return self._mega_evolution
    
    @mega_evolution.setter
    def mega_evolution(self, mega_evolution):
        self._mega_evolution = mega_evolution
    
    @property
    def dynamaaxing(self):
        return self._dynamaaxing
    
    @dynamaaxing.setter
    def dynamaaxing(self, dynamaaxing):
        self._dynamaaxing = dynamaaxing