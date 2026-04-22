import unittest
import random

from dice import RandomDice


class TestDiceInitialization(unittest.TestCase):

    def test_invalid_length_probabilities(self):
        """Test that ValueError is raised for wrong number of probabilities"""
        invalid_probs = [
            [0.5, 0.5],  # Too few
            [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1],  # Too many
            [0.5],  # Way too few
            [0.1] * 10  # Way too many
        ]

        for prob in invalid_probs:
            with self.assertRaises(ValueError):
                RandomDice(prob)

    def test_negative_probabilities(self):
        """Test that ValueError is raised for negative probabilities"""
        invalid_probs = [
            [-0.1, 0.3, 0.3, 0.3, 0.1, 0.1],
            [0.2, -0.2, 0.3, 0.3, 0.2, 0.2],
            [0.1, 0.1, 0.1, 0.1, 0.1, -0.5]
        ]

        for prob in invalid_probs:
            with self.assertRaises(ValueError):
                RandomDice(prob)

    def test_probabilities_not_summing_to_one(self):
        """Test that ValueError is raised when probabilities don't sum to 1"""
        invalid_probs = [
            [0.1, 0.1, 0.1, 0.1, 0.1, 0.1],  # Sum = 0.6
            [0.2, 0.2, 0.2, 0.2, 0.2, 0.2],  # Sum = 1.2
            [0.5, 0.5, 0.5, 0.5, 0.5, 0.5],  # Sum = 3.0
            [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]   # Sum = 0.0
        ]

        for prob in invalid_probs:
            with self.assertRaises(ValueError):
                RandomDice(prob)


class TestDiceRolling(unittest.TestCase):
    def test_single_roll(self):
        """Test rolling dice once"""
        dice = RandomDice()
        result = dice.Roll(1)
        self.assertEqual(len(result), 1)
        self.assertIn(result[0], [1, 2, 3, 4, 5, 6])

    def test_multiple_rolls(self):
        """Test rolling dice multiple times"""
        dice = RandomDice()
        num_rolls = 10
        results = dice.Roll(num_rolls)
        self.assertEqual(len(results), num_rolls)

        for result in results:
            self.assertIn(result, [1, 2, 3, 4, 5, 6])

    def test_custom_probabilities_roll(self):
        """Test rolling with custom probabilities"""
        # Create dice biased towards 6
        biased_prob = [0.1, 0.1, 0.1, 0.1, 0.1, 0.5]
        dice = RandomDice(biased_prob)

        results = dice.Roll(100)

        # Should get some 6s due to bias
        self.assertEqual(len(results), 100)
        for result in results:
            self.assertIn(result, [1, 2, 3, 4, 5, 6])

    def test_zero_rolls(self):
        dice = RandomDice()
        results = dice.Roll(0)
        self.assertEqual(results, [])


if __name__ == '__main__':
    unittest.main()
