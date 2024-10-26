

from Code.DataStructures.Team import Team
from Code.Constructors.PokemonConstructor import PokemonConstructor
from Code.Constructors.BaseConstructor import BaseConstructor
import random

class TeamConstructor(BaseConstructor):
    def __init__(self):
        super().__init__()
        self.pokemon_constructor = PokemonConstructor()

    def create(self, team_data: list):
        if type(team_data[0]) == int:
            return self.create_random(team_data[0])
        pokemons = []
        for pokemon_name in team_data:
            pokemon = self.pokemon_constructor.create(pokemon_name)
            if pokemon:
                pokemons.append(pokemon)
        team = Team(pokemons)
        return team
    
    def create_random(self, n):
        pokemons = random.sample(self.pokemon_constructor.pokemons, n)
        return self.create(pokemons)