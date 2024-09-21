"""
Module containing the class Pokemon.

A Pokemon has stats, moves, level, and other relevant information.
"""

from Code.constants import status_allowed
from Code.move import Move

class Pokemon:
    def __init__(self, name: str, level: int, type: list, ability: str, gender: str, stats: dict, moves: list[Move], shyniness: bool, item: str, weight: float, height: float, tera_type: str) -> None:
        self._name = name
        self._level = level
        self._type = type
        self._ability = ability
        self._weight = weight
        self._height = height
        self._shyniness = shyniness
        self._gender = gender

        self._stats = stats
        self._boosts = {
            'atk': 0,
            'def': 0,
            'spa': 0,
            'spd': 0,
            'spe': 0,
            'acc': 0,
            'eva': 0
        }

        self._moves = moves
        self._tera_type = tera_type
        self._item = item
        self._held_item = item
        
        self._current_hp = 100
        self._status = None
        self._mega_evolved = False
        self._z_crystal = False
        self._dynamaxed = False
        self._terastilized = False


    # Setters and getters
    @property
    def name(self):
        return self._name
    
    @property
    def level(self):
        return self._level
    
    @property
    def type(self):
        return self._type
    
    @property
    def ability(self):
        return self._ability
    
    @property
    def weight(self):
        return self._weight
    
    @property
    def height(self):
        return self._height
    
    @property
    def shyniness(self):
        return self._shyniness
    
    @property
    def gender(self):
        return self.gender
    
    @property
    def stats(self):
        return self._stats
    
    def get_boost(self, stat):
        if stat == 'acc' or stat == 'eva':
            change = 3
        else:
            change = 2
        if self._boosts[stat] < 0:
            return change / (change - self._boosts[stat])
        elif self._boosts[stat] > 0:
            return (change + self._boosts[stat]) / change
        else:
            return 1

    def set_boost(self, stat, value):
        self._boosts[stat] += value
        if self._boosts[stat] > 6:
            self._boosts[stat] = 6
            raise ValueError(f"{self._name}'s {stat} can't go any higher!")
            
        elif self._boosts[stat] < -6:
            self._boosts[stat] = -6
            raise ValueError(f"{self._name}'s {stat} can't go any lower!")
    
    @property
    def moves(self):
        return self._moves
    
    @property
    def tera_type(self):
        return self._tera_type
    
    @property
    def item(self):
        return self._item
    
    @property
    def held_item(self):
        return self._held_item
    
    @held_item.setter
    def held_item(self, item):
        self._held_item = item 
    
    @property
    def current_hp(self):
        return self._current_hp
    
    @current_hp.setter
    def current_hp(self, value):
        self._current_hp += value
        if self._current_hp > 100:
            self._current_hp = 100
        elif self._current_hp <= 0:
            self._current_hp = 0
            self._status = 'FNT'
            print(f'{self._name} has fainted!')

    @property
    def status(self):
        return self._status
    
    @status.setter
    def status(self, value):
        if value not in status_allowed:
            raise ValueError(f'{value} is not a valid status condition!')
        else:
            if self._status is None:
                self._status = value
            else:
                raise ValueError(f'{self._name} is already {self._status}!')


    @property
    def mega_evolved(self):
        return self._mega_evolved
    
    @mega_evolved.setter
    def mega_evolved(self, value):
        if self._dynamaxed:
            raise ValueError(f'{self._name} is already Dynamaxed!')
        elif self._terastilized:
            raise ValueError(f'{self._name} is already Terastilized!')
        else:
            self._mega_evolved = value

    @property
    def z_crystal(self):
        return self._z_crystal
    
    @property
    def dynamaxed(self):
        return self._dynamaxed
    
    @dynamaxed.setter
    def dynamaxed(self, value):
        if self._mega_evolved:
            raise ValueError(f'{self._name} is already Mega Evolved!')
        elif self._terastilized:
            raise ValueError(f'{self._name} is already Terastilized!')
        else:
            self._dynamaxed = value

    @property
    def terastilized(self):
        return self._terastilized
    
    @terastilized.setter
    def terastilized(self, value):
        if self._mega_evolved:
            raise ValueError(f'{self._name} is already Mega Evolved!')
        elif self._dynamaxed:
            raise ValueError(f'{self._name} is already Dynamaxed!')
        else:
            self._terastilized = value

    # Methods

    def __str__(self):
        to_print = f'{self._name} - Level {self._level} - {self._current_hp}% HP'
        if self._status is not None:
            to_print += f' ({self._status})'
        to_print += '\n'
        for stat in self._boosts:
            if stat in ['acc', 'eva']:
                change = 3
            else:
                change = 2
            if self._boosts[stat] < 0:
                to_print += f'{stat.upper()}: * {change / (change - self._boosts[stat])}\n'
            elif self._boosts[stat] > 0:
                to_print += f'{stat.upper()}: * {(change + self._boosts[stat]) / change}\n'
        return to_print
