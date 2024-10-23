import unittest
from Code.DataStructures.Move import Move  # Adjust the import based on your module setup

class TestMove(unittest.TestCase):
    def setUp(self):
        self.move = Move(name="Thunderbolt", type_="Electric", category="Special", power=90, accuracy=100, pp=15, priority=0, target="Single", effect="Paralyzes opponent")

    def test_initial_values(self):
        self.assertEqual(self.move.name, "Thunderbolt")
        self.assertEqual(self.move.type, "Electric")
        self.assertEqual(self.move.category, "Special")
        self.assertEqual(self.move.power, 90)
        self.assertEqual(self.move.accuracy, 100)
        self.assertEqual(self.move.pp, 15)
        self.assertEqual(self.move.priority, 0)
        self.assertEqual(self.move.target, "Single")
        self.assertEqual(self.move.effect, "Paralyzes opponent")

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
