from Code.DataProcessing.PokemonProcessor import PokemonProcessor
from Code.DataProcessing.MovesProcessor import MovesProcessor
from Code.DataProcessing.MovesetProcessor import MovesetProcessor

if __name__ == '__main__':
    pokemon_path = 'RawDatasets/Pokemon/Pokemon.json'
    pokemon_save_path = 'Datasets/Pokemon.json'
    moves_path = 'RawDatasets/Moves/Moves.json'
    moves_save_path = 'Datasets/Moves.json'
    moves_paths = [
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
    movesets_save_path = 'Datasets/Movesets.json'
    pokemon_processor = PokemonProcessor()
    moves_processor = MovesProcessor()
    moveset_processor = MovesetProcessor()
    moveset_processor.process(moves_paths, movesets_save_path)
    pokemon_processor.process(movesets_save_path, pokemon_path, pokemon_save_path)
    moves_processor.process(movesets_save_path, moves_path, moves_save_path)


