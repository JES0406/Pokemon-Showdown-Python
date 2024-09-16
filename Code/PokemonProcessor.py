'''
Module to process the data of the Pokemon dataset

We get all the Pokemon we need in the Pokemon.json file.
'''


import json
from Code.Utils import normalize_name

class PokemonProcessor:
    def __init__(self) -> None:
        self.pokemon_path = 'Raw_Datasets/Pokemon/Pokemon.json'
        self.movesets_path = 'Datasets/Movesets.json'
        self.pokemon_needed = []
        self.pokemon_data = {}

    def process(self):
        self.pokemon_needed = self.get_pokemon_needed()
        self.get_pokemon_data()
        json.dump(self.pokemon_data, open('Datasets/Pokemon.json', 'w'), indent=4)

    def get_pokemon_needed(self):
        pokemon_needed = []
        with open(self.movesets_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            for pokemon in data.keys():
                if pokemon not in pokemon_needed:
                    pokemon_needed.append(pokemon)
        print(f'Got {len(pokemon_needed)} Pokemon')
        return pokemon_needed
    
    def get_pokemon_data(self):
        with open(self.pokemon_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            for pokemon in self.pokemon_needed:
                if normalize_name(pokemon) in data.keys():
                    self.pokemon_data[pokemon] = data[normalize_name(pokemon)]
                else:
                    print(f'Pokemon {pokemon} not found')

        print(f'Got {len(self.pokemon_data)} Pokemon data')
    
if __name__ == '__main__':
    processor = PokemonProcessor()
    processor.process()