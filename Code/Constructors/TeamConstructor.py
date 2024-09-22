

from Code.DataStructures import Team
from Code.Constructors import PokemonConstructor
from Code.Utils import get_choice
from Code.Constructors.BaseConstructor import BaseConstructor

class TeamConstructor(BaseConstructor):
    def __init__(self):
        super().__init__()
        self.pokemon_constructor = PokemonConstructor()

    def create(self, team_data: dict):
        team = Team()
        for pokemon_name in team_data.keys():
            pokemon = self.pokemon_constructor.create(pokemon_name)
            if pokemon:
                team.add_pokemon(pokemon)
        return team