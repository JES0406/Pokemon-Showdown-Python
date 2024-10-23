import unittest
from Code.Constructors.MoveConstructor import MoveConstructor

class TestMove(unittest.TestCase):
    def setUp(self):
        self.move = MoveConstructor().create("thunderbolt")

    def test_initial_values(self):
        self.assertEqual(self.move.name, "Thunderbolt")
        self.assertEqual(self.move.type, "Electric")
        self.assertEqual(self.move.category, "Special")
        self.assertEqual(self.move.power, 90)
        self.assertEqual(self.move.accuracy, 100)
        self.assertEqual(self.move.pp, 15)
        self.assertEqual(self.move.priority, 0)
        self.assertEqual(self.move.target, "normal")
        self.assertEqual(self.move.flags, {
            "protect": 1,
            "mirror": 1,
            "metronome": 1
        })
        self.assertEqual(self.move.desc, "Has a 10% chance to paralyze the target.")

    def test_accuracy_setter(self):
        self.move.accuracy = 120
        self.assertEqual(self.move.accuracy, 100)

    def test_pp_setter(self):
        self.move.pp = 20
        self.assertEqual(self.move.pp, 15)  # Should be capped at base_pp

    def test_use_method(self):
        self.move.use()
        self.assertEqual(self.move.pp, 14)
        # Use until PP is 0
        while self.move.pp > 0:
            self.move.use()
        self.assertEqual(self.move.pp, 0)
        with self.assertRaises(ValueError):
            self.move.use()  # Should raise an exception

if __name__ == '__main__':
    unittest.main()
