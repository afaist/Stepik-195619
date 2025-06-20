from code_8_1_12 import gen_squares
import unittest


class TestGenSquares(unittest.TestCase):
    def test_gen_squares(self):
        self.assertEqual(list(gen_squares(10)), [1, 4, 9, 16, 25, 36, 49, 64, 81, 100])
        self.assertEqual(list(gen_squares(0)), [])
        self.assertEqual(list(gen_squares(-1)), [])
        self.assertEqual(list(gen_squares(1)), [1])
        self.assertEqual(list(gen_squares(2)), [1, 4])

    def test_gen_squares_2(self):
        self.assertEqual(list(gen_squares(10)), [1, 4, 9, 16, 25, 36, 49, 64, 81, 100])
        self.assertEqual(list(gen_squares(0)), [])
        self.assertEqual(list(gen_squares(-1)), [])
        self.assertEqual(list(gen_squares(1)), [1])
        self.assertEqual(list(gen_squares(2)), [1, 4])
