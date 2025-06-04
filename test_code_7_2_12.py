from code_7_2_12 import sum_digits
import unittest


class TestSumDigits(unittest.TestCase):
    def test_sum_digits(self):
        self.assertEqual(sum_digits(10), 1)
        self.assertEqual(sum_digits(99), 18)
        self.assertEqual(sum_digits(32), 5)
