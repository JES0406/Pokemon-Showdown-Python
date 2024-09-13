import unittest
from unittest.mock import MagicMock
from Code.pokemon import Pokemon
from Code.move import Move
from Code.player import Player
from Code.battle import Battle

class TestBattle(unittest.TestCase):

    def setUp(self):
        # Set up sample moves
        self.move1 = Move(name="Thunderbolt", power=90, category="Special", type="Electric", priority=0, accuracy=100, pp=15, target="Single", effect="Paralysis")
        self.move2 = Move(name="Vine Whip", power=45, category="Physical", type="Grass", priority=0, accuracy=100, pp=25, target="Single", effect="None")

        # Set up sample Pokémon
        self.pokemon1 = Pokemon(name="Pikachu", stats={'atk': 55, 'def': 40, 'spa': 50, 'spd': 50, 'spe': 90, 'hp': 35}, level=50,
                                type=["Electric"], ability="Static", gender="Male", moves=[self.move1], shyniness=False, item="Light Ball")
        self.pokemon2 = Pokemon(name="Bulbasaur", stats={'atk': 49, 'def': 49, 'spa': 65, 'spd': 65, 'spe': 45, 'hp': 45}, level=50,
                                type=["Grass", "Poison"], ability="Overgrow", gender="Male", moves=[self.move2], shyniness=False, item="Miracle Seed")

        # Set up sample players
        self.player1 = Player(name="Ash", team=[self.pokemon1])
        self.player2 = Player(name="Brock", team=[self.pokemon2])

        # Set up the battle instance
        self.battle = Battle(players=[self.player1, self.player2])

    def test_initial_battle_state(self):
        # Test if the battle initializes correctly
        self.assertEqual(len(self.battle.players), 2)
        self.assertEqual(self.battle.players[0].name, "Ash")
        self.assertEqual(self.battle.players[1].name, "Brock")

    def test_player_team(self):
        # Test if players have the correct Pokémon in their team
        self.assertEqual(self.player1.team[0].name, "Pikachu")
        self.assertEqual(self.player2.team[0].name, "Bulbasaur")

    def test_pokemon_moves(self):
        # Test if the Pokémon have the correct moves
        self.assertEqual(self.pokemon1.moves[0].name, "Thunderbolt")
        self.assertEqual(self.pokemon2.moves[0].name, "Vine Whip")

    def test_battle_order(self):
        # Test if the battle order is correctly determined
        self.battle.turn_order(self.move1, self.move2)
        self.assertEqual(self.battle.current_turn_order, [0, 1])

    def test_battle_run(self):
        # Mock the input function to test battle flow
        self.battle.run(testing = True)
        self.assertTrue(self.battle.is_finished())

if __name__ == '__main__':
    unittest.main()
