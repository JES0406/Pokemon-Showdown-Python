"""
Module containing the class Pokemon.

A Pokemon has stats, moves, level, and other relevant information.
"""

from Code.constants import status_allowed, volatile_status_allowed
from Code.DataStructures.Move import Move

class Pokemon:
    def __init__(self, 
                 name: str,
                 types: list = None, 
                 stats: dict = None, 
                 height: float = None,
                 weight: float = None, 
                 otherFormes: list = None, 
                 tier: str = None, 
                 shyniness: bool = None,
                 gender: str = None,
                 level: int = None, 
                 ability: str = None, 
                 item: str = None, 
                 moves: list = None,
                 tera_type: str = None):
        """
        Initialize the Pokémon class with relevant attributes.
        :param name: Name of the Pokémon.
        :param types: List of Pokémon types (e.g., ['Fire', 'Flying']).
        :param stats: Dictionary containing base stats (e.g., {'hp': 78, 'atk': 84, 'def': 78, ...}).
        :param height: Height of the Pokémon (in meters).
        :param weight: Weight of the Pokémon (in kilograms).
        :param otherFormes: Other forms of the Pokémon, if any.
        :param shyniness: Boolean indicating if the Pokémon is shiny.
        :param tier: Competitive tier of the Pokémon (e.g., 'OU', 'UU').
        :param gender: Gender distribution (e.g., 'Male', 'Female', or 'Genderless').
        :param level: Level of the Pokémon (e.g., 50, 100).
        :param ability: Name of the Pokémon's ability.
        :param item: Name of the item the Pokémon is holding.
        :param moves: List of moves the Pokémon can use.
        """
        self._name = name
        self._types = types if types is not None else []
        self._height = height
        self._weight = weight
        self._level = level
        self._gender = gender
        self._otherFormes = otherFormes if otherFormes is not None else []
        self._tier = tier
        self._shyniness = shyniness

        self._stats = stats if stats is not None else {}
        self._boosts = {
            'atk': 0,
            'def': 0,
            'spa': 0,
            'spd': 0,
            'spe': 0,
            'acc': 0,
            'eva': 0
        }

        self._ability = ability if ability is not None else {}
        self._item = item if item is not None else {}
        self._held_item = item if item is not None else {}
        self._moves = moves if moves is not None else {}
        self._tera_type = tera_type

        self._current_hp = self._stats['hp']
        self._status = None
        self._volatile_status = None
        self._mega_evolved = False
        self._z_crystal = False
        self._dynamaxed = False
        self._terastilized = False

        self.grounded = False



    # Setters and getters
    @property
    def name(self):
        return self._name
    
    @property
    def types(self):
        return self._types
    
    @property
    def height(self):
        return self._height
    
    @property
    def weight(self):
        return self._weight
    
    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, value):
        if value < 1 or value > 100:
            raise ValueError('Level must be between 1 and 100!')
        else:
            self._level = value

    @property
    def gender(self):
        return self._gender
    
    @property
    def otherFormes(self):
        return self._otherFormes
    
    @property
    def tier(self):
        return self._tier

    @property
    def shyniness(self):
        return self._shyniness

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
    def ability(self):
        return self._ability
    
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
    def moves(self):
        return self._moves
    
    @property
    def tera_type(self):
        return self._tera_type
    
    @property
    def current_hp(self):
        return self._current_hp
    
    @current_hp.setter
    def current_hp(self, value):
        self._current_hp = value
        if self._current_hp > self._stats['hp']:
            self._current_hp = self._stats['hp']
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
    def volatile_status(self):
        return self._volatile_status
    
    @volatile_status.setter
    def volatile_status(self, value):
        if value not in volatile_status_allowed:
            raise ValueError(f'{value} is not a valid volatile status condition!')
        else:
            self._volatile_status = value

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

    @property
    def grounded(self):
        return self._grounded
    
    @grounded.setter
    def grounded(self, value):
        self._grounded = value

    # Methods
    def __str__(self):
        to_print = f'{self._name} - Level {self._level} - {self._current_hp} HP'
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
