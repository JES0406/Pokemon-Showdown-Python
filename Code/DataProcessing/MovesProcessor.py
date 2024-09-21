'''
Module to process the moves of the game

We get all the moves we need in the Movesets.json file.
'''

import json
from Code.Utils import normalize_name
from Code.DataProcessing.BaseProcessor import BaseProcessor

class MovesProcessor(BaseProcessor):
    def __init__(self, data: dict = None):
        """
        Initialize the MovesProcessor with raw data.
        """
        super().__init__(data)

    def process(self, movesets_path: str = 'Datasets/Movesets.json', moves_path: str = 'Datasets/Moves.json', save_path: str = 'Datasets/Moves.json'):
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
        move_data = {normalize_name(move): self.transform_move_data(self.data[normalize_name(move)]) for move in moves_needed if normalize_name(move) in self.data.keys()}
        return move_data

    def transform_move_data(self, move_info: dict) -> dict:
        """
        Transform the raw move data into a more structured format.
        :param move_info: Raw move data
        :return: Transformed move data
        """

        # Check if move_info is a dictionary, if not return None or handle the error
        if not isinstance(move_info, dict):
            print(f"Error: Expected a dictionary but got {type(move_info)}")
            return None

        # Now proceed to transform the move data as usual
        transformed_move = {
            "num": move_info.get("num", None),
            "name": move_info.get("name", None),
            "type": move_info.get("type", None),
            "category": move_info.get("category", None),
            "pp": move_info.get("pp", None),
            "basePower": move_info.get("basePower", None),
            "accuracy": move_info.get("accuracy", None),
            "priority": move_info.get("priority", None),
            "flags": {}
        }

        transformed_move = self.handle_flags(transformed_move, move_info)
        transformed_move = self.handle_additional_effects(transformed_move, move_info)
        transformed_move = self.handle_target(transformed_move, move_info)
        transformed_move = self.handle_z_max_moves(transformed_move, move_info)
        transformed_move = self.handle_optional_effects(transformed_move, move_info)

        return transformed_move

    def handle_flags(self, transformed_move: dict, move_info: dict) -> dict:
        '''Method to handle the flags of the move
        :param transformed_move: The transformed move data
        :param move_info: The raw move data
        :return: The transformed move data with the flags included
        '''
        # Handling flags - only include the relevant true flags
        for flag in ['protect', 'mirror', 'contact', 'bullet', 'sound', 'heal', 'recharge', 'distance', 'snatch', 'metronome']:
            if flag in move_info.get("flags", {}):
                transformed_move["flags"][flag] = move_info["flags"].get(flag, False)

        return transformed_move

    def handle_additional_effects(self, transformed_move: dict, move_info: dict) -> dict:
        '''Method to handle the additional effects of the move
        :param transformed_move: The transformed move data
        :param move_info: The raw move data
        :return: The transformed move data with the additional effects included
        '''

        # Handling secondary effects (if not None)
        if move_info.get("secondary") is not None:
            transformed_move["secondary"] = {
                "chance": move_info["secondary"].get("chance", None),
                "status": move_info["secondary"].get("status", None),
                "boosts": move_info["secondary"].get("boosts", None)
            }
        else:
            transformed_move["secondary"] = None

        return transformed_move

    def handle_target(self, transformed_move: dict, move_info: dict) -> dict:
        '''Method to handle the target of the move
        :param transformed_move: The transformed move data
        :param move_info: The raw move data
        :return: The transformed move data with the target included
        '''
        # Handling target
        transformed_move["target"] = move_info.get("target", None)

        return transformed_move

    def handle_z_max_moves(self, transformed_move: dict, move_info: dict) -> dict:
        '''Method to handle the Z-Move and Max Move specifics
        :param transformed_move: The transformed move data
        :param move_info: The raw move data
        :return: The transformed move data with the Z-Move and Max Move specifics included
        '''
        # Handling Z-Move specifics
        if "zMove" in move_info:
            transformed_move["zMove"] = {
                "boost": move_info["zMove"].get("boost", None),
                "effect": move_info["zMove"].get("effect", None),
                "basePower": move_info["zMove"].get("basePower", None)
            }
            
        # Handling Max Move specifics
        if "maxMove" in move_info:
            transformed_move["maxMove"] = {
                "basePower": move_info["maxMove"].get("basePower", None)
            }

        return transformed_move
    
    def handle_optional_effects(self, transformed_move: dict, move_info: dict) -> dict:
        '''Method to handle the optional effects of the move
        :param transformed_move: The transformed move data
        :param move_info: The raw move data
        :return: The transformed move data with the optional effects included
        '''
        # Handling additional optional effects (recoil, heal, crit ratio, etc.)
        optional_effects = ['recoil', 'heal', 'critRatio', 'drain', 'forceSwitch', 'selfBoost', 'weather']
        for effect in optional_effects:
            if effect in move_info:
                transformed_move[effect] = move_info.get(effect, None)

        return transformed_move

if __name__ == '__main__':
    processor = MovesProcessor()
    processor.process()
