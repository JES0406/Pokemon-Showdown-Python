'''
This file contains the class Team, which is used to represent a team in the game.

A team is formed by 6 pokemon
'''

from Code.DataStructures.Pokemon import Pokemon

class Team:
    def __init__(self, pokemon: list[Pokemon] = []):
        """
        Initialize the Team with the pokemon.
        :param pokemon: List of pokemon in the team.
        """
        self.pokemon = pokemon

    def validate_team(self):
        """
        Validate the team.
        """
        if len(self.pokemon) < 1 or len(self.pokemon) > 6:
            raise ValueError('A team must have between 1 and 6 pokemon.')
        for pokemon in self.pokemon:
            if not isinstance(pokemon, Pokemon):
                raise ValueError('A team must be formed by pokemon.')
            
    def add_pokemon(self, pokemon: Pokemon):
        """
        Add a pokemon to the team.
        :param pokemon: Pokemon to add to the team.
        """
        if len(self.pokemon) == 6:
            raise ValueError('A team can only have 6 pokemon.')
        self.pokemon.append(pokemon)

    def __str__(self):
        return f"Team: {self.pokemon}"
    
    def __repr__(self):
        return f"Team({self.pokemon})"
    
    def __len__(self):
        return len(self.pokemon)
    
    def __getitem__(self, index):
        return self.pokemon[index]
    
    def __setitem__(self, index, value):
        self.pokemon[index] = value