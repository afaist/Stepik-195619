from code_3_5_11 import lstrip
import unittest


class TestLstrip(unittest.TestCase):
    def test_lstrip(self):
        data = [0, 0, 1, 0, 2, 3]
        self.assertEqual(lstrip(data, 0), [1, 0, 2, 3])
        self.assertEqual(data, [0, 0, 1, 0, 2, 3])

    def test_zero(self):
        data = []
        self.assertEqual(lstrip(data, 0), [])
        self.assertEqual(data, [])

    def test_ones(self):
        data = [1, 1, 1, 1]
        self.assertEqual(lstrip(data, 1), [])
        self.assertEqual(data, [1, 1, 1, 1])
