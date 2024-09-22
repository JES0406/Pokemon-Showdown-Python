'''
Module for creating Move objects

Creates a Move, searching for the Move's stats in the database
'''


from Code.DataStructures.Move import Move
from Code.Constructors.BaseConstructor import BaseConstructor

class MoveConstructor(BaseConstructor):
    def __init__(self):
        super().__init__()
        self._data = self.load_data('Datasets/Moves.json')

    def create(self, name: str):
        if name in self._data.keys():
            move_data = self._data[name]
            self.move = Move(**move_data)
        else:
            raise ValueError(f"Move {name} not found")
        
    def get_structure(self):
        return self.move