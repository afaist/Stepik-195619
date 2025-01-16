from code_3_6_13 import multiply
import unittest


class TestMultiply(unittest.TestCase):
    def test_multiply(self):
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(0, 3), 0)
        self.assertEqual(multiply(-2, 3), -6)
        self.assertEqual(multiply(), 1)
