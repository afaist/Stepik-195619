from code_7_3_4 import power
import unittest


class TestPower(unittest.TestCase):
    def test_power(self):
        self.assertEqual(power(2, 4), 16)
        self.assertEqual(power(3, 4), 81)
        self.assertEqual(power(2, 0), 1)
        self.assertEqual(power(0, 0), 1)
        self.assertEqual(power(2, 5), 32)
        self.assertEqual(power(2, 10), 1024)
