'''
Module to process the moves of the game

We get all the moves we need in the Movesets.json file.
'''

from Code.Utils import normalize_name
from Code.DataProcessing.BaseProcessor import BaseProcessor
from Code.DataProcessing.MoveTransformer import MoveTransformer

class MovesProcessor(BaseProcessor):
    def __init__(self, data: dict = None):
        """
        Initialize the MovesProcessor with raw data.
        """
        super().__init__(data)
        self.transformer = MoveTransformer()

    def process(self, movesets_path: str = 'Datasets/Movesets.json', moves_path: str = 'RawDatasets/Moves/Moves.json', save_path: str = 'Datasets/Moves.json'):
        """
        Load data, process it based on the needed moves, and save the processed data.
        :param movesets_path: Path to the file containing the needed moves list.
        :param moves_path: Path to the raw moves data file.
        :param save_path: Path where processed data will be saved.
        """
        self.data = self.load_data(moves_path)
        if not self.validate_data():
            raise ValueError("Data validation failed")
        
        moves_needed = self.get_needed(movesets_path)
        self.move_data = self.get_data(moves_needed)
        self.move_data = self.correct_data(self.move_data)
        self.data = self.move_data
        self.save_data(save_path)

    def get_needed(self, movesets_path: str) -> list:
        """
        Get the list of needed moves from the movesets file.
        :param movesets_path: Path to the file containing the movesets.
        :return: List of needed move names.
        """
        moves_needed = set()
        movesets_data = self.load_data(movesets_path)
        for pokemon in movesets_data.keys():
            if "roles" in movesets_data[pokemon].keys():
                for role in movesets_data[pokemon]["roles"]:
                    data = movesets_data[pokemon]["roles"][role]
            else:
                data = movesets_data[pokemon]

            if "moves" in data.keys():
                moves = self.get_moves(movesets_data[pokemon])
                moves_needed.update(moves)
            else:
                print(f'Pokemon {pokemon} has no moves')

        return moves_needed

    def get_moves(self, data:dict) -> list:
        """
        Get the list of moves from the data.
        :param data: Data containing the moves.
        :return: List of move names.
        """
        moves = set()
        for role in data['roles'].keys():
            role_data = data['roles'][role]
            if "moves" in role_data.keys():
                moves.update(role_data["moves"])
        return list(moves)
    
    def get_data(self, moves_needed: list):
        """
        Fetch data for the moves in the moves_needed list.
        :param moves_needed: List of move names to process.
        """
        move_data = {normalize_name(move): self.transformer.transform(self.data[normalize_name(move)]) for move in moves_needed if normalize_name(move) in self.data.keys()}
        return move_data

    def correct_data(self, data: dict):
        """
        Correct the data by removing unneeded fields.
        """
        for move in data.keys():
            data[move] = self.remove_unneeded(data[move])
        return data

    def remove_unneeded(self, data: dict):
        """
        Remove unneeded moves from the data.
        """
        return data
if __name__ == '__main__':
    processor = MovesProcessor()
    processor.process()
