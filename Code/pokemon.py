'''
Module containg the class Pokemon.

A pokemon has stats, moves, level and other relevant information.
'''

from constants import status_allowed

class Pokemon:
    def __init__(self, name: str, level: int, type: list, ability: str, gender:str, stats: dict, moves: list, shyiness: bool, item: str):
        self._name = name
        self._level = level
        self._type = type
        self._ability = ability
        self._stats = stats
        self._moves = moves
        self._shyniness = shyiness
        self._current_hp = 100
        self._status = None
        self._boosts = {
            'atk': 0,
            'def': 0,
            'spa': 0,
            'spd': 0,
            'spe': 0,
            'acc': 0,
            'eva': 0
        }
        self.mega_evolved = False
        self.z_crystal = False
        self.dynamaxed = False
        self.terastilized = False # Normally a string indicating the type of terastilization
        self.item = item
        self.held_item = item

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
    def stats(self):
        return self._stats
    
    @property
    def moves(self):
        return self._moves
    
    @property
    def shyniness(self):
        return self._shyniness
    
    @property
    def current_hp(self):
        return self._current_hp
    
    @current_hp.setter
    def current_hp(self, value):
        self._current_hp += value
        if self._current_hp > 100:
            self._current_hp = 100
        elif self._current_hp < 0:
            self._current_hp = 0
            self._status = 'Fainted'

    @property
    def status(self):
        return self._status
    
    @status.setter
    def status(self, value):
        if value not in status_allowed:
            print(f'{value} is not a valid status condition!')
        else:
            if self._status == None:
                self._status = value
            else:
                print(f'{self._name} is already {self._status}!')

    @property
    def boosts(self, stat):
        return self._boosts[stat]
    
    @boosts.setter
    def boosts(self, stat, value):
        self._boosts[stat] += value
        if self._boosts[stat] > 6:
            print(f'{self._name}\'s {stat} can\'t go any higher!')
            self._boosts[stat] = 6
        elif self._boosts[stat] < -6:
            print(f'{self._name}\'s {stat} can\'t go any lower!')
            self._boosts[stat] = -6

    @property
    def mega_evolved(self):
        return self._mega_evolved
    
    @mega_evolved.setter
    def mega_evolved(self, value):
        if self._dinamaxed:
            print(f'{self._name} is already dinamaxed!')
        elif self.terastilized:
            print(f'{self._name} is already terastilized!')
        else:
            self._mega_evolved = value

    @property
    def z_crystal(self):
        return self._z_crystal
    
    @property
    def dinamaxed(self):
        return self._dinamaxed
    
    @dinamaxed.setter
    def dinamaxed(self, value):
        if self._mega_evolved:
            print(f'{self._name} is already mega evolved!')
        elif self.terastilized:
            print(f'{self._name} is already terastilized!')
        else:
            self._dinamaxed = value

    @property
    def terastilized(self):
        return self._terastilized
    
    @terastilized.setter
    def terastilized(self, value):
        if self._mega_evolved:
            print(f'{self._name} is already mega evolved!')
        elif self._dinamaxed:
            print(f'{self._name} is already dinamaxed!')
        else:
            self._terastilized = value

    @property
    def item(self):
        return self._item
    
    @property
    def held_item(self):
        return self._held_item
    
    @held_item.setter
    def held_item(self, item):
        self._held_item = item 

    # Methods

    def __str__(self):
        print(f'{self._name} - Level {self._level} - {self._current_hp}% HP')
        if self._status != None:
            print(f' ({self._status})', end='')
        print()
        for stat in self._boosts:
            if stat == 'acc' or stat == 'eva':
                change = 3
            else:
                change = 2
            if self._boosts[stat] < 0:
                print(f'{stat.upper()}: * {change/(change - self._boosts[stat])}')
            elif self._boosts[stat] > 0:
                print(f'{stat.upper()}: * {(change + self._boosts[stat])/change}')