from code_3_9_8 import calculate_high_low_avg
import unittest


class TestCalculate(unittest.TestCase):
    def test_calculate(self):
        self.assertAlmostEqual(calculate_high_low_avg(1, 2, 3), 2)
        self.assertAlmostEqual(calculate_high_low_avg(1, 2, 3, 4), 2.5)
        self.assertAlmostEqual(calculate_high_low_avg(1, 2, 3, 4, 5), 3)
