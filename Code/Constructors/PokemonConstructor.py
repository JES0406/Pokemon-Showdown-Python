'''
Module for creating Pokemon objects

Creates a Pokemon, searching for the Pokemon's stats and moveset in the database
'''

import random
from Code.DataStructures.Pokemon import Pokemon
from Code.Constructors.BaseConstructor import BaseConstructor
from Code.Constructors.PokemonStatsCalculator import PokemonStatsCalculator
from Code.Constructors.PokemonMoveSelector import PokemonMoveSelector
from Code.Utils import get_choice, normalize_name

class PokemonConstructor(BaseConstructor):
    def __init__(self):
        super().__init__()
        self._data = self.load_data('Datasets/Pokemon.json')
        self._moveset_data = self.load_data('Datasets/Movesets.json')
        self._pokemons = list(self._moveset_data.keys())
        self.stats_calculator = PokemonStatsCalculator()
        self.move_selector = PokemonMoveSelector()

    @property
    def pokemons(self):
        return self._pokemons

    def create(self, name: str):
        name = normalize_name(name)
        if name in self._data.keys() and name in self._moveset_data.keys():
            pokemon_data = self._data[name]
            moveset_data = self._moveset_data[name]

            role = get_choice(list(moveset_data['roles'].keys()), weights=[role['weight'] for role in moveset_data['roles'].values()])[0]
            role_data = moveset_data['roles'][role]

            pokemon = Pokemon(
                name=name,
                types=pokemon_data['type'],
                stats=self.stats_calculator.calculate_stats(
                    pokemon_data['stats'],
                    self.set_ivs_evs(self._moveset_data[name]['roles'][role]['ivs']),
                    self.set_ivs_evs(self._moveset_data[name]['roles'][role]['evs']),
                    moveset_data['level']
                ),
                height=pokemon_data['height'],
                weight=pokemon_data['weight'],
                otherFormes=pokemon_data.get('otherFormes', []),
                tier=pokemon_data.get('tier', None),
                shyniness=True if random.randint(1, 8192) == 1 else False,
                gender=pokemon_data.get('gender', random.choice(['M', 'F'])),
                level=moveset_data['level'],
                ability=get_choice(list(role_data['abilities'].keys()), weights=list(role_data['abilities'].values()))[0],
                item=get_choice(list(role_data['items'].keys()), weights=list(role_data['items'].values()))[0],
                moves=self.move_selector.get_moves(role_data, moveset_data),
                tera_type=role_data.get('tera_type', pokemon_data['type'][0]),
            )
            return pokemon
        else:
            raise ValueError(f"Pokemon {name} not found in the database")
    def set_ivs_evs(self, data: dict):
        return {
            'hp': data.get('hp', 0),
            'atk': data.get('atk', 0),
            'def': data.get('def', 0),
            'spa': data.get('spa', 0),
            'spd': data.get('spd', 0),
            'spe': data.get('spe', 0)
        }
    