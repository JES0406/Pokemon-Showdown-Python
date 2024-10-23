'''
Module for unitary tests.

This module contains the unitary tests for the Pokemon class.
'''
import unittest
from Code.Constructors.PokemonConstructor import PokemonConstructor
import unittest

# Assuming your Pokemon class is defined above this or imported from another module.

class TestPokemon(unittest.TestCase):
    
    def setUp(self):
        # Create a test instance of Pokemon
        self.constructor = PokemonConstructor()
        self.Pokemon = self.constructor.create("abomasnow")
        # self.Pokemon = Pokemon(
        #     name="Pikachu", 
        #     level=25, 
        #     types=["Electric"], 
        #     ability="Static", 
        #     gender="Male", 
        #     stats={"atk": 55, "def": 40, "spa": 50, "spd": 50, "spe": 90}, 
        #     moves=["Thunderbolt", "Quick Attack", "Iron Tail", "Electro Ball"], 
        #     shyniness=False, 
        #     item="Light Ball"
        # )
    
    def test_initialization(self):
        # Test whether the Pokemon is initialized correctly
        self.assertEqual(self.Pokemon.name, "Pikachu")
        self.assertEqual(self.Pokemon.level, 25)
        self.assertEqual(self.Pokemon.current_hp, 100)
        self.assertIsNone(self.Pokemon.status)
        self.assertFalse(self.Pokemon.mega_evolved)
        self.assertFalse(self.Pokemon.dynamaxed)
        self.assertFalse(self.Pokemon.terastilized)
    
    def test_stat_boost(self):
        # Test stat boosts
        self.Pokemon.set_boost('atk', 3)
        self.assertEqual(self.Pokemon.get_boost('atk'), (2+3)/2)
        
        # Test boost limit
        with self.assertRaises(ValueError):
            self.Pokemon.set_boost('atk', 4)
        self.assertEqual(self.Pokemon.get_boost('atk'), (2+6)/2)
    
    def test_stat_drop(self):
        # Test stat drops
        self.Pokemon.set_boost('def', -2)
        self.assertEqual(self.Pokemon.get_boost('def'), 2/(2+2))
        
        # Test drop limit
        with self.assertRaises(ValueError):
            self.Pokemon.set_boost('def', -5)
        self.assertEqual(self.Pokemon.get_boost('def'), 2/(2+6))

    def test_hp_changes(self):
        # Test increasing HP beyond 100%
        self.Pokemon.current_hp = 110
        self.assertEqual(self.Pokemon.current_hp, 100)  # Capped at 100
        
        # Test decreasing HP below 0%
        self.Pokemon.current_hp = -150
        self.assertEqual(self.Pokemon.current_hp, 0)
        self.assertEqual(self.Pokemon.status, 'FNT')
    
    def test_status_condition(self):
        # Test setting valid status
        self.Pokemon.status = "par"
        self.assertEqual(self.Pokemon.status, "par")
        
        # Test trying to set an invalid status
        with self.assertRaises(ValueError):
            self.Pokemon.status = "Happy"

        # Test setting status when another is placed
        with self.assertRaises(ValueError):
            self.Pokemon.status = "PSN"
    
    def test_mega_evolution(self):
        # Test Mega Evolution
        self.Pokemon.mega_evolved = True
        self.assertTrue(self.Pokemon.mega_evolved)
    
    def test_dynamax(self):
        # Test Dynamax activation
        self.Pokemon.dynamaxed = True
        self.assertTrue(self.Pokemon.dynamaxed)
    
    def test_terastilize(self):
        # Test Terastilization
        self.Pokemon.terastilized = True
        self.assertTrue(self.Pokemon.terastilized)
    
    def test_prevent_conflicting_forms(self):
        # Test that Dynamax prevents Mega Evolution
        self.Pokemon.dynamaxed = True
        with self.assertRaises(ValueError):
            self.Pokemon.mega_evolved = True

    def test_item_change(self):
        # Test changing held item
        self.assertEqual(self.Pokemon.held_item, "Light Ball")
        self.Pokemon.held_item = "Oran Berry"
        self.assertEqual(self.Pokemon.held_item, "Oran Berry")
    
    def test_string_representation(self):
        # Test the __str__ method for a basic string representation
        expected_str = "Pikachu - Level 25 - 100% HP"
        print(self.Pokemon)
        self.assertTrue(expected_str in str(self.Pokemon))

if __name__ == '__main__':
    unittest.main()
