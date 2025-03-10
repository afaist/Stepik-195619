from code_5_6_9 import double_odd_numbers
import unittest


class TestDoubleOddNumbers(unittest.TestCase):
    def test_double_odd_numbers(self):
        self.assertEqual(double_odd_numbers([1, 2, 3, 4, 5]), [2, 6, 10])
        self.assertEqual(double_odd_numbers([6, 8, 10, 2]), [])
        self.assertEqual(
            double_odd_numbers([-43, 91, 932, 9201, 32, 93]), [-86, 182, 18402, 186]
        )
