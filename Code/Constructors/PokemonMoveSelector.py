from Code.Utils import get_choice
from Code.Constructors.MoveConstructor import MoveConstructor

class PokemonMoveSelector:
    def __init__(self):
        self.move_builder = MoveConstructor()

    def get_moves(self, role_data, moveset_data):
        if len(role_data['moves']) > 4:
            moves = get_choice(role_data['moves'], 4)
        else:
            moves = role_data['moves']
        return [self.move_builder.create(move) for move in moves]