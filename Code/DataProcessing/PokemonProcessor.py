'''
Module to process the data of the Pokemon dataset

We get all the Pokemon we need in the Pokemon.json file.
'''


from Code.Utils import normalize_name
from Code.DataProcessing.BaseProcessor import BaseProcessor
from Code.DataProcessing.PokemonTransformer import PokemonTransformer

class PokemonProcessor(BaseProcessor):
    def __init__(self, data=None):
        """
        Initialize the PokemonProcessor with raw data.
        :param data: Raw Pokémon data (as a dictionary or loaded from a file).
        """
        super().__init__(data)
        self.processed_data = {}  # Stores the processed Pokémon data
        self.transformer = PokemonTransformer()
    
    def process(self, moveset_path, data_path:str, save_path:str = 'Datasets/Pokemon.json'):
        """
        Load data, process it based on the needed Pokémon, and save the processed data.
        :param moveset_path: Path to the file containing the needed Pokémon list.
        :param data_path: Path to the raw Pokémon data file.
        :param save_path: Path where processed data will be saved.
        """
        self.data = self.load_data(data_path)
        if not self.validate_data():
            raise ValueError("Data validation failed")
        
        needed_pokemon = self.get_needed(moveset_path)
        self.get_data(needed_pokemon)
        self.save_data(save_path)

    def get_needed(self, moveset_path: str) -> list:
        """
        Get the list of needed Pokémon from the moveset file.
        :param moveset_path: Path to the file containing the moveset.
        :return: List of needed Pokémon names.
        """
        needed_pokemon = []
        moveset_data = self.load_data(moveset_path)
        needed_pokemon = [normalize_name(pokemon) for pokemon in moveset_data.keys()]
        return needed_pokemon
    
    def get_data(self, needed_pokemon: list):
        """
        Fetch data for the Pokémon in the needed_pokemon list.
        :param needed_pokemon: List of Pokémon names to process.
        """

        for name in needed_pokemon:
            if name in self.data.keys():
                self.process_pokemon(name, self.data)
            else:
                print(f'Pokemon {name} not found in data')
        self.data = self.processed_data

    def process_pokemon(self, name: str, data: dict):
        """
        Process individual Pokémon data and normalize relevant fields.
        :param pokemon: Name of the Pokémon being processed.
        :param data: Raw data of the Pokémon.
        """
        if name in data:
            # Assign tier based on Pokémon attributes
            data = self.assign_tier(name, data)
            
            # Extract and process relevant Pokémon information
            self.extract_pokemon_data(name, data[name])
        else:
            print(f'Pokemon {name} not found in provided data')
        return data

    def assign_tier(self, name: str, data: dict) -> dict:
        """
        Assign tier to the Pokémon, handling special cases like Keldeo.
        """
        if 'tier' not in data:
            if 'baseSpecies' in data:
                base_species = normalize_name(data['baseSpecies'])
                data['tier'] = self.processed_data.get(base_species, {}).get('tier', None)

        # Special handling for Keldeo
        if "keldeo" in name:
            data['tier'] = 'OU'

        return data

    def extract_pokemon_data(self, pokemon: str, data: dict):
        self.processed_data[pokemon] = self.transformer.transform(data)
    
if __name__ == '__main__':
    processor = PokemonProcessor()
    processor.process('Datasets/Movesets.json', 'Raw_Datasets/Pokemon/Pokemon.json')