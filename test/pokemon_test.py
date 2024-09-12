'''
Module for unitary tests.

This module contains the unitary tests for the Pokemon class.
'''

import unittest
from Code.pokemon import Pokemon
import unittest

# Assuming your Pokemon class is defined above this or imported from another module.

class TestPokemon(unittest.TestCase):
    
    def setUp(self):
        # Create a test instance of Pokemon
        self.pikachu = Pokemon(
            name="Pikachu", 
            level=25, 
            type=["Electric"], 
            ability="Static", 
            gender="Male", 
            stats={"atk": 55, "def": 40, "spa": 50, "spd": 50, "spe": 90}, 
            moves=["Thunderbolt", "Quick Attack", "Iron Tail", "Electro Ball"], 
            shyniness=False, 
            item="Light Ball"
        )
    
    def test_initialization(self):
        # Test whether the Pokemon is initialized correctly
        self.assertEqual(self.pikachu.name, "Pikachu")
        self.assertEqual(self.pikachu.level, 25)
        self.assertEqual(self.pikachu.current_hp, 100)
        self.assertIsNone(self.pikachu.status)
        self.assertFalse(self.pikachu.mega_evolved)
        self.assertFalse(self.pikachu.dynamaxed)
        self.assertFalse(self.pikachu.terastilized)
    
    def test_stat_boost(self):
        # Test stat boosts
        self.pikachu.set_boost('atk', 3)
        self.assertEqual(self.pikachu.get_boost('atk'), 3)
        
        # Test boost limit
        self.pikachu.set_boost('atk', 4)  # Should not exceed +6
        self.assertEqual(self.pikachu.get_boost('atk'), 6)
    
    def test_stat_drop(self):
        # Test stat drops
        self.pikachu.set_boost('def', -2)
        self.assertEqual(self.pikachu.get_boost('def'), -2)
        
        # Test drop limit
        self.pikachu.set_boost('def', -5)  # Should not go below -6
        self.assertEqual(self.pikachu.get_boost('def'), -6)

    def test_hp_changes(self):
        # Test increasing HP beyond 100%
        self.pikachu.current_hp = 10
        self.assertEqual(self.pikachu.current_hp, 100)  # Capped at 100
        
        # Test decreasing HP below 0%
        self.pikachu.current_hp = -150
        self.assertEqual(self.pikachu.current_hp, 0)
        self.assertEqual(self.pikachu.status, 'FNT')
    
    def test_status_condition(self):
        # Test setting valid status
        self.pikachu.status = "PAR"
        self.assertEqual(self.pikachu.status, "PAR")
        
        # Test trying to set an invalid status
        self.pikachu.status = "Happy"
        self.assertNotEqual(self.pikachu.status, "Happy")  # Invalid status should not be set
    
    def test_mega_evolution(self):
        # Test Mega Evolution
        self.pikachu.mega_evolved = True
        self.assertTrue(self.pikachu.mega_evolved)
    
    def test_dynamax(self):
        # Test Dynamax activation
        self.pikachu.dynamaxed = True
        self.assertTrue(self.pikachu.dynamaxed)
    
    def test_terastilize(self):
        # Test Terastilization
        self.pikachu.terastilized = True
        self.assertTrue(self.pikachu.terastilized)
    
    def test_prevent_conflicting_forms(self):
        # Test that Dynamax prevents Mega Evolution
        self.pikachu.dynamaxed = True
        self.pikachu.mega_evolved = True  # Should fail
        self.assertFalse(self.pikachu.mega_evolved)
        
        # Test that Mega Evolution prevents Terastilization
        self.pikachu.mega_evolved = True
        self.pikachu.terastilized = True  # Should fail
        self.assertFalse(self.pikachu.terastilized)

    def test_item_change(self):
        # Test changing held item
        self.assertEqual(self.pikachu.held_item, "Light Ball")
        self.pikachu.held_item = "Oran Berry"
        self.assertEqual(self.pikachu.held_item, "Oran Berry")
    
    def test_string_representation(self):
        # Test the __str__ method for a basic string representation
        expected_str = "Pikachu - Level 25 - 100% HP\n"
        self.assertTrue(expected_str in str(self.pikachu))

if __name__ == '__main__':
    unittest.main()
