import unittest
from Code.Constructors.BattleConstructor import BattleConstructor
import random

class TestBattle(unittest.TestCase):

    def setUp(self):
        self.battle_constructor = BattleConstructor()
        self.battle = self.battle_constructor.create({
            "players": [
                {
                    "name": "Ash",
                    "team": ["Pikachu", "Charizard"]
                },
                {
                    "name": "Brock",
                    "team": ["Venusaur"]
                }
            ]
        })
        self.player1 = self.battle.players[0]
        self.player2 = self.battle.players[1]

        self.pokemon1 = self.player1.current_pokemon
        self.pokemon2 = self.player2.current_pokemon

        self.move1 = self.pokemon1.moves[0]
        self.move2 = self.pokemon2.moves[0]

    def test_initial_battle_state(self):
        # Test if the battle initializes correctly
        self.assertEqual(len(self.battle.players), 2)
        self.assertEqual(self.player1.name, "Ash")
        self.assertEqual(self.player2.name, "Brock")
        self.assertEqual(self.battle.turn, 0)
        self.assertIsNone(self.battle.winner)
        self.assertIsNone(self.battle.weather)
        self.assertIsNone(self.battle.terrain)

    def test_player_team(self):
        # Test if players have the correct Pokémon in their team
        self.assertEqual(self.pokemon1.name, "pikachu")
        self.assertEqual(self.pokemon2.name, "venusaur")

    def test_turn_order_by_priority(self):
        # Test if the turn order is determined correctly based on move priority
        self.move1.priority = 1
        self.move2.priority = 0
        self.battle.turn_order(self.move1, self.move2)
        self.assertEqual(self.battle.current_turn_order, [0, 1])

        self.move1.priority = 0
        self.move2.priority = 1
        self.battle.turn_order(self.move1, self.move2)
        self.assertEqual(self.battle.current_turn_order, [1, 0])

    def test_turn_order_by_speed(self): 
        # Test if the turn order is determined by speed if priority is equal
        self.move1.priority = 0
        self.move2.priority = 0
        self.pokemon1.stats['spe'] = 90
        self.pokemon2.stats['spe'] = 45
        self.battle.turn_order(self.move1, self.move2)
        self.assertEqual(self.battle.current_turn_order, [0, 1])

    def test_random_turn_order_for_same_speed(self):
        # Test if the turn order is randomized when both Pokémon have the same speed
        self.pokemon1.stats['spe'] = 45
        self.pokemon2.stats['spe'] = 45
        random.seed(1)  # Seed the randomness to make the test deterministic
        self.battle.turn_order(self.move1, self.move2)
        self.assertEqual(self.battle.current_turn_order, [0, 1])  # Based on the random seed

    def test_damage_calculation(self):
        # Test the damage calculation
        damage = self.battle.calculate_damage(self.move1, self.pokemon1, self.pokemon2)
        self.assertGreater(damage, 0)  # Ensure damage is calculated

    def test_apply_damage(self):
        # Test applying damage to a Pokémon
        initial_hp = self.pokemon2.current_hp
        damage = self.battle.calculate_damage(self.move1, self.pokemon1, self.pokemon2)
        self.battle.apply_damage(self.move1, self.pokemon1, self.pokemon2, damage)
        self.assertLess(self.pokemon2.current_hp, initial_hp)  # HP should decrease after damage

    def test_switch_logic(self):
        # Test if Pokémon can be switched correctly
        initial_pokemon = self.player1.current_pokemon
        self.player1.switch_pokemon(1)  # Switch to Charmander
        self.assertNotEqual(self.player1.current_pokemon, initial_pokemon)  # Pokémon should change
        self.assertEqual(self.player1.current_pokemon.name, "charizard")  # Switched to Charmander
        
    def test_battle_run(self):
        # Mock the input function to test battle flow and check if it finishes
        self.assertFalse(self.battle.is_finished())
        self.battle.run()
        self.assertTrue(self.battle.is_finished())

if __name__ == '__main__':
    unittest.main()
