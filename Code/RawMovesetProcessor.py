'''
Module for processing raw moveset data
'''

import json
import csv

class RawMovesetProcessor:
    def __init__(self):
        self.paths = [
            'Raw_Datasets/Movesets/gen9randombattle.json',
            'Raw_Datasets/Movesets/gen8randombattle.json',
            'Raw_Datasets/Movesets/gen8bdsprandombattle.json',
            'Raw_Datasets/Movesets/gen7randombattle.json',
            'Raw_Datasets/Movesets/gen7letsgorandombattle.json',
            'Raw_Datasets/Movesets/gen6randombattle.json',
            'Raw_Datasets/Movesets/gen5randombattle.json',
            'Raw_Datasets/Movesets/gen4randombattle.json',
            'Raw_Datasets/Movesets/gen3randombattle.json',
            'Raw_Datasets/Movesets/gen2randombattle.json',
            'Raw_Datasets/Movesets/gen1randombattle.json'
        ]
        self.pokemon_names = []
        self.pokemon_data = {}

    def process(self):
        for path in self.paths:
            n_before = len(self.pokemon_names)
            with open(path, 'r', encoding='utf-8') as file:
                data = json.load(file)
                self.process_data(data)

            print(f'Processed {path}, {len(self.pokemon_names) - n_before} new pokemon')
        json.dump(self.pokemon_data, open('Datasets/Movesets.json', 'a'), indent=4)
        print(f'Total pokemon: {len(self.pokemon_names)}')
        

    def process_data(self, data):
        for pokemon in data.keys():
            self.process_pokemon(pokemon, data[pokemon])

    def process_pokemon(self, pokemon: str, data: dict):
        if pokemon not in self.pokemon_names:
            self.pokemon_names.append(pokemon)
            self.pokemon_data[pokemon] = data

if __name__ == '__main__':
    processor = RawMovesetProcessor()
    processor.process()
        