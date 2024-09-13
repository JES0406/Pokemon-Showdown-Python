import unittest
from Code.player import Player
from Code.pokemon import Pokemon

class TestPlayer(unittest.TestCase):

    def setUp(self):
        # Create Pokémon instances for the team
        self.pikachu = Pokemon("Pikachu", 50, ["Electric"], "Static", "Male", 
                               {"hp": 35, "atk": 55, "def": 40, "spa": 50, "spd": 50, "spe": 90},
                                 ["Thunderbolt", "Quick Attack", "Iron Tail", "Electro Ball"], False, "Light Ball")
        self.charizard = Pokemon("Charizard", 50, ["Fire", "Flying"], "Blaze", "Male", 
                                 {"hp": 78, "atk": 84, "def": 78, "spa": 109, "spd": 85, "spe": 100},
                                 ["Flamethrower", "Air Slash", "Dragon Claw", "Fire Blast"], False, "Charizardite X")
        self.bulbasaur = Pokemon("Bulbasaur", 50, ["Grass", "Poison"], "Overgrow", "Male",
                                    {"hp": 45, "atk": 49, "def": 49, "spa": 65, "spd": 65, "spe": 45},
                                    ["Vine Whip", "Razor Leaf", "Seed Bomb", "Sludge Bomb"], False, "Miracle Seed")
        
        
        # Create Player instance with a valid team
        self.player = Player("Ash", [self.pikachu, self.charizard, self.bulbasaur])

    def test_initialization(self):
        """Test that Player class initializes correctly with valid input."""
        self.assertEqual(self.player.name, "Ash")
        self.assertEqual(len(self.player.team), 3)
        self.assertEqual(self.player.current_pokemon.name, "Pikachu")

    def test_invalid_team_size(self):
        """Test that initializing a Player with an invalid team size raises an exception."""
        with self.assertRaises(ValueError):
            invalid_player = Player("Brock", [])  # Empty team should raise ValueError
        
        with self.assertRaises(ValueError):
            too_large_team = [self.pikachu] * 7  # More than 6 Pokémon
            invalid_player = Player("Misty", too_large_team)

    def test_invalid_team_members(self):
        """Test that initializing a Player with invalid team members raises an exception."""
        with self.assertRaises(ValueError):
            invalid_team = [self.pikachu, "NotAPokemon", self.bulbasaur]
            invalid_player = Player("Gary", invalid_team)

    def test_switch_pokemon(self):
        """Test that switching the current Pokémon works as expected."""
        self.player.current_pokemon = 1
        self.assertEqual(self.player.current_pokemon.name, "Charizard")

        self.player.current_pokemon = 2
        self.assertEqual(self.player.current_pokemon.name, "Bulbasaur")

    def test_invalid_pokemon_index(self):
        """Test that setting an invalid Pokémon index raises an IndexError."""
        with self.assertRaises(IndexError):
            self.player.current_pokemon = 5  # Out of range (team has 3 Pokémon)

    def test_dynamax(self):
        """Test that Dynamaxing a Pokémon works and limits to one use."""
        self.player.dynamaxing = True
        self.assertTrue(self.player.dynamaxing)
        
        self.assertEqual(self.player.current_pokemon.name, "Pikachu")
        self.player.current_pokemon.dynamaxed = True  # Dynamax Pikachu
        self.assertTrue(self.player.current_pokemon.dynamaxed)

        # Dynamaxing another Pokémon should not be allowed
        self.player.current_pokemon = 1  # Switch to Charizard
        with self.assertRaises(ValueError):
            self.player.dynamaxing = True  # Dynamaxing already used

    def test_mega_evolution(self):
        """Test that Mega Evolution works and restricts to one Pokémon."""
        self.assertFalse(self.player.mega_evolution)
        self.assertEqual(self.player.current_pokemon.name, "Pikachu")

        # Mega Evolve Charizard
        self.player.current_pokemon = 1  # Switch to Charizard
        self.player.mega_evolution = True
        self.assertTrue(self.player.mega_evolution)
        self.assertTrue(self.player.current_pokemon.mega_evolved)

    def test_terastallization(self):
        """Test that Terastallization works and restricts to one Pokémon."""
        self.assertFalse(self.player.terastization)
        
        # Terastallize Bulbasaur
        self.player.current_pokemon = 2  # Switch to Bulbasaur
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
        self.player.current_pokemon = 2  # Bulbasaur
        self.player.dynamaxing = True
        self.assertTrue(self.player.dynamaxing)

        with self.assertRaises(ValueError):
            self.player.terastization = True  # Bulbasaur cannot be Terastallized after Dynamaxing


if __name__ == '__main__':
    unittest.main()
