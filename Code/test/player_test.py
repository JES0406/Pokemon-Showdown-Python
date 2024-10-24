import unittest
from Code.Constructors.PlayerConstructor import PlayerConstructor

class TestPlayer(unittest.TestCase):

    def setUp(self):
        # Create Pokémon instances for the team
        
        
        # Create Player instance with a valid team
        self.player_constructor = PlayerConstructor()
        # print(f"Id of the player constructor: {id(self.player_constructor)}")
        self.player = self.player_constructor.create({
            "name": "Ash",
            "team": ["pikachu", "charizard", "venusaur"],
        })

        self.pikachu = self.player.team[0]
        self.charizard = self.player.team[1]
        self.venusaur = self.player.team[2]

    def tearDown(self):
        del self.player
        del self.pikachu
        del self.charizard
        del self.venusaur

    def test_initialization(self):
        """Test that Player class initializes correctly with valid input."""
        self.assertEqual(self.player.name, "Ash")
        self.assertEqual(len(self.player.team), 3)
        self.assertEqual(self.player.current_pokemon.name, "pikachu")

    def test_invalid_team_size(self):
        """Test that initializing a Player with an invalid team size raises an exception."""
        with self.assertRaises(ValueError):
            invalid_player = self.player_constructor.create({
                "name": "Ash",
                "team": []  # Empty team
            })
            print(invalid_player)
        
        with self.assertRaises(ValueError):
            too_large_team = [self.pikachu] * 7  # More than 6 Pokémon
            invalid_player = self.player_constructor.create({
                "name": "Ash",
                "team": too_large_team
            })

    def test_invalid_team_members(self):
        """Test that initializing a Player with invalid team members raises an exception."""
        with self.assertRaises(ValueError):
            invalid_team = [self.pikachu, "NotAPokemon", self.venusaur]
            invalid_player = self.player_constructor.create({
                "name": "Ash",
                "team": invalid_team
            })

    def test_switch_pokemon(self):
        """Test that switching the current Pokémon works as expected."""
        self.player.current_pokemon = 1
        self.assertEqual(self.player.current_pokemon.name, "charizard")

        self.player.current_pokemon = 2
        self.assertEqual(self.player.current_pokemon.name, "venusaur")

    def test_invalid_pokemon_index(self):
        """Test that setting an invalid Pokémon index raises an IndexError."""
        with self.assertRaises(IndexError):
            self.player.current_pokemon = 5  # Out of range (team has 3 Pokémon)

    def test_dynamax(self):
        """Test that Dynamaxing a Pokémon works and limits to one use."""
        self.player.dynamaxing = True
        self.assertTrue(self.player.dynamaxing)
        
        self.assertEqual(self.player.current_pokemon.name, "pikachu")
        self.player.current_pokemon.dynamaxed = True  # Dynamax Pikachu
        self.assertTrue(self.player.current_pokemon.dynamaxed)

        # Dynamaxing another Pokémon should not be allowed
        self.player.current_pokemon = 1  # Switch to Charizard
        with self.assertRaises(ValueError):
            self.player.dynamaxing = True  # Dynamaxing already used

    def test_mega_evolution(self):
        """Test that Mega Evolution works and restricts to one Pokémon."""
        self.assertFalse(self.player.mega_evolution)
        self.assertEqual(self.player.current_pokemon.name, "pikachu")

        # Mega Evolve Charizard
        self.player.current_pokemon = 1  # Switch to Charizard
        self.player.mega_evolution = True
        self.assertTrue(self.player.mega_evolution)
        self.assertTrue(self.player.current_pokemon.mega_evolved)

    def test_terastallization(self):
        """Test that Terastallization works and restricts to one Pokémon."""
        self.assertFalse(self.player.terastization)
        
        # Terastallize venusaur
        self.player.current_pokemon = 2  # Switch to venusaur
        self.player.terastization = True
        self.assertTrue(self.player.terastization)
        self.assertTrue(self.player.current_pokemon.terastilized)

    def test_dynamax_and_mega(self):
        """Test that a Pokémon cannot be both Dynamaxed and Mega Evolved."""
        self.player.current_pokemon = 1  # Charizard
        self.player.mega_evolution = True
        self.assertTrue(self.player.mega_evolution)

        with self.assertRaises(ValueError):
            self.player.dynamaxing = True  # Charizard cannot be Dynamaxed after Mega Evolving

    def test_dynamax_and_terastallize(self):
        """Test that a Pokémon cannot be both Dynamaxed and Terastallized."""
        self.player.current_pokemon = 2  # venusaur
        self.player.dynamaxing = True
        self.assertTrue(self.player.dynamaxing)

        with self.assertRaises(ValueError):
            self.player.terastization = True  # venusaur cannot be Terastallized after Dynamaxing

    def test_switch_logic(self):
        # Test if Pokémon can be switched correctly
        initial_pokemon = self.player.current_pokemon
        self.player.switch_pokemon(1)  # Switch to Charizard
        self.assertNotEqual(self.player.current_pokemon, initial_pokemon)  # Pokémon should change
        self.assertEqual(self.player.current_pokemon.name, "charizard")

    def test_invalid_switch_logic(self):
        # Test invalid switch cases
        with self.assertRaises(IndexError):
            self.player.switch_pokemon(3)  # Attempt to switch to an invalid index

        with self.assertRaises(ValueError):
            self.player.switch_pokemon(0)  # Attempt to switch to the current Pokémon

        self.player.current_pokemon.current_hp = -100
        self.player.current_pokemon = 1
        with self.assertRaises(ValueError):
            self.player.switch_pokemon(0)  # Attempt to switch to a fainted Pokémon


if __name__ == '__main__':
    unittest.main()
