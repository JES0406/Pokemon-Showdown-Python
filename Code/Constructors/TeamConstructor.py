

from Code.DataStructures.Team import Team
from Code.Constructors.PokemonConstructor import PokemonConstructor
from Code.Constructors.BaseConstructor import BaseConstructor

class TeamConstructor(BaseConstructor):
    def __init__(self):
        super().__init__()
        self.pokemon_constructor = PokemonConstructor()

    def create(self, team_data: dict):
        pokemons = []
        for pokemon_name in team_data:
            pokemon = self.pokemon_constructor.create(pokemon_name)
            if pokemon:
                pokemons.append(pokemon)
        team = Team(pokemons)
        return team