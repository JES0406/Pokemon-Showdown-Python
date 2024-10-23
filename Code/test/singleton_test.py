import unittest
from Code.Constructors.PlayerConstructor import PlayerConstructor

class TestSingleton(unittest.TestCase):
    def test_players_have_different_teams(self):
        player_constructor = PlayerConstructor()
        
        player_1 = player_constructor.create({
            "name": "Ash",
            "team": ["pikachu", "charizard", "raichu"]
        })
        
        player_2 = player_constructor.create({
            "name": "Misty",
            "team": ["abomasnow", "golduck", "gyarados"]
        })
        
        # Assert that the team objects for both players are different
        self.assertNotEqual(id(player_1.team), id(player_2.team))
        
        # Assert that individual Pokémon objects are different
        for i in range(3):
            self.assertNotEqual(id(player_1.team[i]), id(player_2.team[i]))

if __name__ == '__main__':
    unittest.main()