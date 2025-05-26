from code_6_6_12 import luhn_algorithm
import unittest


class TestLuhnAlgorithm(unittest.TestCase):
    def test_luhn_algorithm(self):
        self.assertTrue(luhn_algorithm(3942682966937054))
        self.assertFalse(luhn_algorithm(2553514623369426))
        self.assertFalse(luhn_algorithm(255351462336942))
        self.assertTrue(luhn_algorithm(1217040151414995))
        self.assertTrue(luhn_algorithm(4012888888881881))
        self.assertTrue(luhn_algorithm(4111111111111111))
