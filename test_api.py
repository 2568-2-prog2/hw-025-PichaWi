import unittest

from dice import RandomDice
from basic_client import call_api


class TestApi(unittest.TestCase):

    url = "http://127.0.0.1:8081/roll_dice"

    def test_api_response(self):
        data = {
            "probabilities": [0.1, 0.2, 0.3, 0.1, 0.2, 0.1],  # Valid
            "number_of_random": 10
        }
        print(data)
        response = call_api(self.url, data)
        self.assertIsNotNone(response)
        self.assertIsInstance(response, dict)
        self.assertEqual(response.get('status'), 'success')

    def test_api_invalid_probabilities(self):
        data = {
            # Invalid probabilities (sum > 1)
            "probabilities": [0.1, 0.2, 0.3, 0.1, 0.2, 0.2],
            "number_of_random": 10
        }
        print(data)
        response = call_api(self.url, data)
        self.assertIsNotNone(response)
        self.assertIsInstance(response, dict)
        self.assertEqual(response.get('status'), 'error')

    def test_api_invalid_json(self):
        data = "This is not a valid JSON"
        print(data)
        response = call_api(self.url, data)
        self.assertIsNotNone(response)
        self.assertIsInstance(response, dict)
        self.assertEqual(response.get('status'), 'error')

    def test_api_missing_fields(self):
        data = {
            "number_of_random": 10  # Missing field
        }
        print(data)
        response = call_api(self.url, data)
        self.assertIsNotNone(response)
        self.assertIsInstance(response, dict)
        self.assertEqual(response.get('status'), 'error')

    def test_api_zero_rolls(self):
        data = {
            "probabilities": [0.1, 0.2, 0.3, 0.1, 0.2, 0.1],
            "number_of_random": 0  # Zero rolls
        }
        print(data)
        response = call_api(self.url, data)
        self.assertIsNotNone(response)
        self.assertIsInstance(response, dict)
        self.assertEqual(response.get('status'), 'success')
        self.assertEqual(response.get('dices'), [])


if __name__ == '__main__':
    unittest.main()
