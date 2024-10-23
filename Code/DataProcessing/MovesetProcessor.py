'''
Module for processing raw moveset data
'''
from Code.Utils import normalize_name
from Code.DataProcessing.BaseProcessor import BaseProcessor

class MovesetProcessor(BaseProcessor):
    def __init__(self, file_paths: list = None):
        """
        Initialize the MovesetProcessor with raw data.
        :param data: Raw moveset data (as a dictionary or loaded from a file).
        """
        super().__init__()
        self.file_paths = file_paths
        self.pokemon_names = []  # Stores the names of the Pokémon
        self.moveset_data = {}  # Stores the raw moveset data
        self.data = {}  # Stores the processed moveset data
    
    # We need to override the load_data method to handle the multiple files
    def load_data_from_files(self, file_paths: list) -> dict:
        """
        Load data from multiple files.
        :param file_paths: List of paths to the data files.
        """
        data = {}
        for i, path in enumerate(file_paths):
            data[i] = self.load_data(path)
        return data

    def process(self, paths: list, save_path: str = 'Datasets/Movesets.json')-> None:
        """
        Process the raw moveset data.
        :param paths: List of paths to the raw moveset data files.
        :param save_path: Path to save the processed data.
        """
        self.file_paths = paths
        self.moveset_data = self.load_data_from_files(self.file_paths)
        self.process_data(self.moveset_data)
        self.save_data(save_path)
            

    def process_data(self, data):
        for i in data.keys():
            for pokemon in data[i].keys():
                self.process_pokemon(pokemon.lower(), data[i][pokemon])

    def process_pokemon(self, pokemon: str, data: dict):
        if pokemon not in self.pokemon_names:
            self.pokemon_names.append(pokemon)
            data = self.normalize_data(data)
            self.data[pokemon.lower()] = data

    def normalize_data(self, data: dict):
        data = self.normalize_roles(data)
        data = self.normalize_stats(data)
        return data
    
    def normalize_roles(self, data: dict):
        if 'roles' not in data.keys():
            data['roles'] = {
                'standard': {
                    'weight': 1,
                    'moves': {normalize_name(move): data['moves'][move] for move in data['moves']},
                    'items': data['items'] if 'items' in data.keys() else None,
                }
            }

            data.pop('moves')
            if 'items' in data.keys():
                data.pop('items')
        else:
            for role in data['roles'].keys():
                data['roles'][role]['moves'] = {normalize_name(move): data['roles'][role]['moves'][move] for move in data['roles'][role]['moves']}
        return data
    
    def normalize_stats(self, data: dict):
        for role in data['roles'].keys():
            if 'ivs' not in data['roles'][role].keys():
                data['roles'][role]['ivs'] = {
                    'hp': 31,
                    'atk': 31,
                    'def': 31,
                    'spa': 31,
                    'spd': 31,
                    'spe': 31
                }
            if 'evs' not in data['roles'][role].keys():
                data['roles'][role]['evs'] = {
                    'hp': 0,
                    'atk': 0,
                    'def': 0,
                    'spa': 0,
                    'spd': 0,
                    'spe': 0
                }
        return data

if __name__ == '__main__':
    paths = [
            'RawDatasets/Movesets/gen9randombattle.json',
            'RawDatasets/Movesets/gen8randombattle.json',
            'RawDatasets/Movesets/gen8bdsprandombattle.json',
            'RawDatasets/Movesets/gen7randombattle.json',
            'RawDatasets/Movesets/gen7letsgorandombattle.json',
            'RawDatasets/Movesets/gen6randombattle.json',
            'RawDatasets/Movesets/gen5randombattle.json',
            'RawDatasets/Movesets/gen4randombattle.json',
            'RawDatasets/Movesets/gen3randombattle.json',
            'RawDatasets/Movesets/gen2randombattle.json',
            'RawDatasets/Movesets/gen1randombattle.json'
        ]

    processor = MovesetProcessor()
    processor.process(paths)
        