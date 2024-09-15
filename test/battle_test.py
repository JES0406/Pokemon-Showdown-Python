import unittest
from Code.pokemon import Pokemon
from Code.move import Move
from Code.player import Player
from Code.battle import Battle
import random

class TestBattle(unittest.TestCase):

    def setUp(self):
        # Set up sample moves
        self.move1 = Move(name="Thunderbolt", power=90, category="Special", type="Electric", priority=0, accuracy=100, pp=15, target="Single", effect="Paralysis")
        self.move2 = Move(name="Vine Whip", power=45, category="Physical", type="Grass", priority=0, accuracy=100, pp=25, target="Single", effect="None")
        self.move3 = Move(name="Ember", power=40, category="Special", type="Fire", priority=0, accuracy=100, pp=25, target="Single", effect="Burn")

        # Set up sample Pokémon
        self.pokemon1 = Pokemon(name="Pikachu", stats={'atk': 55, 'def': 40, 'spa': 50, 'spd': 50, 'spe': 90, 'hp': 35}, level=50,
                                type=["Electric"], ability="Static", gender="Male", moves=[self.move1], shyniness=False, item="Light Ball")
        self.pokemon2 = Pokemon(name="Bulbasaur", stats={'atk': 49, 'def': 49, 'spa': 65, 'spd': 65, 'spe': 45, 'hp': 45}, level=50,
                                type=["Grass", "Poison"], ability="Overgrow", gender="Male", moves=[self.move2], shyniness=False, item="Miracle Seed")
        self.pokemon3 = Pokemon(name="Charmander", stats={'atk': 52, 'def': 43, 'spa': 60, 'spd': 50, 'spe': 65, 'hp': 39}, level=50,
                                type=["Fire"], ability='Blaze', gender='Male', moves=[self.move3], shyniness=False, item='Charcoal')
        

        # Set up sample players
        self.player1 = Player(name="Ash", team=[self.pokemon1, self.pokemon3])
        self.player2 = Player(name="Brock", team=[self.pokemon2])

        # Set up the battle instance
        self.battle = Battle(players=[self.player1, self.player2])

    def test_initial_battle_state(self):
        # Test if the battle initializes correctly
        self.assertEqual(len(self.battle.players), 2)
        self.assertEqual(self.battle.players[0].name, "Ash")
        self.assertEqual(self.battle.players[1].name, "Brock")
        self.assertEqual(self.battle.turn, 0)
        self.assertIsNone(self.battle.winner)
        self.assertIsNone(self.battle.weather)
        self.assertIsNone(self.battle.terrain)

    def test_player_team(self):
        # Test if players have the correct Pokémon in their team
        self.assertEqual(self.player1.team[0].name, "Pikachu")
        self.assertEqual(self.player2.team[0].name, "Bulbasaur")

    def test_pokemon_moves(self):
        # Test if the Pokémon have the correct moves
        self.assertEqual(self.pokemon1.moves[0].name, "Thunderbolt")
        self.assertEqual(self.pokemon2.moves[0].name, "Vine Whip")

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
        self.assertEqual(self.player1.current_pokemon.name, "Charmander")
        
    def test_battle_run(self):
        # Mock the input function to test battle flow and check if it finishes
        self.assertFalse(self.battle.is_finished())
        self.battle.run(testing = True)
        self.assertTrue(self.battle.is_finished())

if __name__ == '__main__':
    unittest.main()
