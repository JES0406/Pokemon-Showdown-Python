'''
Module for testing in batch mode.

This module is used to test the battle system of the game in batch mode.
'''

import unittest

from Code.battle import Battle
from Code.move import Move
from Code.player import Player
from Code.pokemon import Pokemon

from test.battle_test import TestBattle
from test.move_test import TestMove
from test.player_test import TestPlayer
from test.pokemon_test import TestPokemon

def test_suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestBattle))
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestMove))
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestPlayer))
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestPokemon))
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(test_suite())