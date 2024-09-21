'''
Module for creating Pokemon objects

Creates a Pokemon, searching for the Pokemon's stats and moveset in the database
'''

import random
import json
from Code.pokemon import Pokemon
from Code.move import Move
from Code.MoveConstructor import MoveConstructor

class PokemonConstructor:
    def __init__(self):
        self.pokemon_data = json.load(open('Datasets/Pokemon.json', 'r'))
        self.moveset_data = json.load(open('Datasets/Movesets.json', 'r'))
        self.move_builder = MoveConstructor()
        self.pokemon = None

    def create_pokemon(self, name: str):
        if name in self.pokemon_data.keys():
            pokemon_data = self.pokemon_data[name]
            moveset_data = self.moveset_data[name]

            role = self.get_choice(moveset_data['roles'])

            if len(moveset_data['roles'][role]['moves']) > 4:
                moves_ = self.get_choice(moveset_data['roles'][role]['moves'], 4)
            else:
                moves_ = moveset_data['roles'][role]['moves']
                
            self.pokemon = Pokemon(
                name=name,
                level=moveset_data['level'],
                type=pokemon_data['type'],
                ability=self.get_choice(moveset_data['roles'][role]['abilities']),
                weight=pokemon_data['weight'],
                height=pokemon_data['height'],
                shyniness=True if random.randint(1, 8192) == 1 else False,
                gender=pokemon_data['gender'] if pokemon_data['gender'] is not None else random.choice(['M', 'F']),
                stats=pokemon_data['stats'],
                moves=[self.move_builder.create_move(move) for move in moves_],
                tera_type=moveset_data['roles'][role]['tera_type'] if 'tera_type' in moveset_data['roles'][role].keys() else pokemon_data['type'][0],
                item=self.get_choice(moveset_data['roles'][role]['items']) if 'items' in moveset_data['roles'][role].keys() else None               
            )

    def get_choice(self, data: dict, n: int = 1):
        options = list(data.keys())
        weights = list(data.values())
        return random.choices(options, weights=weights, k=n)
    