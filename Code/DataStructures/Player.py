'''
module for player class

The player class is used to represent a player in the game.
The player has attributes such as name, team, and current pokemon and terastization, mega evolution and dynamaxing flags.
'''

from Code.DataStructures.Team import Team


class Player:
    def __init__(self, name: str, team: Team, id_: int):
        self._id = id_
        self._name = name
        self._team = team

        self.team_validations()
        self._current_pokemon = 0 # Default current pokemon is the first one
        self._terastization = False
        self._mega_evolution = False
        self._dynamaxing = False
        self._move = None
        self._switch = False

    def team_validations(self):
        self._team.validate_team()

    # Setters and getters
    @property
    def id(self):
        return self._id

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
        if pokemon_index < 0 or pokemon_index >= len(self._team):
            raise IndexError('Invalid pokemon index')
        self._current_pokemon = pokemon_index
    
    @property
    def terastization(self):
        return self._terastization
    
    @terastization.setter
    def terastization(self, terastization):
        if self._terastization and terastization:
            raise ValueError('Terastization already used')
        self._team[self._current_pokemon].terastilized = True
        self._terastization = terastization
    
    @property
    def mega_evolution(self):
        return self._mega_evolution
    
    @mega_evolution.setter
    def mega_evolution(self, mega_evolution):
        if self._mega_evolution and mega_evolution:
            raise ValueError('Mega evolution already used')
        self._team[self._current_pokemon].mega_evolved = True
        self._mega_evolution = mega_evolution
    
    @property
    def dynamaxing(self):
        return self._dynamaxing
    
    @dynamaxing.setter
    def dynamaxing(self, dynamaxing):
        if self._dynamaxing and dynamaxing:
            raise ValueError('Dynamaxing already used')
        self._team[self._current_pokemon].dynamaxed = True
        self._dynamaxing = dynamaxing

    @property
    def move(self):
        return self._move
    
    @move.setter
    def move(self, move_index):
        if move_index < 0 or move_index >= len(self._team[self._current_pokemon].moves):
            raise IndexError('Invalid move index')
        self._move = self._team[self._current_pokemon].moves[move_index]

    @property
    def switch(self):
        return self._switch
    
    @switch.setter
    def switch(self, switch):
        if type(switch) != bool:
            raise ValueError('Switch must be a boolean')
        self._switch = switch

    # Methods
    def __str__(self):
        return f'Player {self._name} with team {self._team}'
    
    def switch_pokemon(self, pokemon_index: int):
        if pokemon_index < 0 or pokemon_index >= len(self._team):
            raise IndexError('Invalid pokemon index')
        elif self._team[pokemon_index].status == 'FNT':
            raise ValueError('Cannot switch to a fainted pokemon')
        elif pokemon_index == self._current_pokemon:
            raise ValueError('Pokemon is already on the field')
        self._current_pokemon = pokemon_index
        self.switch = True

    def __repr__(self) -> str:
        return f'{self.id}, {self.name}'