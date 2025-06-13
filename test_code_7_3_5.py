from code_7_3_5 import gcd
import unittest


class TestGCD(unittest.TestCase):
    def test_gcd(self):
        self.assertEqual(gcd(10, 15), 5)
        self.assertEqual(gcd(21, 35), 7)
        self.assertEqual(gcd(0, 21), 21)
        self.assertEqual(gcd(21, 0), 21)
        self.assertEqual(gcd(0, 0), 0)
        self.assertEqual(gcd(7, 19), 1)
