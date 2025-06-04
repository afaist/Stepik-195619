from code_7_2_15 import double_fact
import unittest


class TestDoubleFact(unittest.TestCase):
    def test_double_fact(self):
        self.assertEqual(double_fact(6), 48)
        self.assertEqual(double_fact(1), 1)
        self.assertEqual(double_fact(2), 2)
        self.assertEqual(double_fact(3), 3)
        self.assertEqual(double_fact(4), 8)
        self.assertEqual(double_fact(5), 15)
