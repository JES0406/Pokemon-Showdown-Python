'''
Module to process the moves of the game

We get all the moves we need in the Movesets.json file.
'''

import json
from Code.Utils import normalize_name

class MovesProcessor:
    def __init__(self):
        self.moves_path = 'Raw_Datasets/Moves/Moves.json'
        self.movesets_path = 'Datasets/Movesets.json'
        self.moves_needed = []
        self.move_data = {}


    def process(self):
        self.moves_needed = self.get_moves_needed()
        self.get_move_data()
        json.dump(self.move_data, open('Datasets/Moves.json', 'w'), indent=4)

    def get_moves_needed(self):
        moves_needed = []
        with open(self.movesets_path, 'r') as file:
            data = json.load(file)
            for pokemon in data.keys():
                if "roles" in data[pokemon].keys():
                    for role in data[pokemon]["roles"]:
                        role_data = data[pokemon]["roles"][role]
                        if "moves" in role_data.keys():
                            for move in role_data["moves"]:
                                if move not in moves_needed:
                                    moves_needed.append(move)
                else:
                    if "moves" in data[pokemon].keys():
                        for move in data[pokemon]["moves"]:
                            if move not in moves_needed:
                                moves_needed.append(move)

        print(f'Got {len(moves_needed)} moves')
        return moves_needed
    
    def get_move_data(self):
        with open(self.moves_path, 'r') as file:
            data = json.load(file)
            for move in self.moves_needed:
                if normalize_name(move) in data.keys():
                    self.move_data[move] = data[normalize_name(move)]
                else:
                    print(f'Move {move} not found')

        print(f'Got {len(self.move_data)} move data')

if __name__ == '__main__':
    processor = MovesProcessor()
    processor.process()
