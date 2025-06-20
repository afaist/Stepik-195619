from code_8_1_19 import my_range_gen
import unittest


class TestMyRangeGen(unittest.TestCase):
    def test_my_range_gen(self):
        self.assertEqual(list(my_range_gen(5)), [0, 1, 2, 3, 4])
        self.assertEqual(list(my_range_gen(2, 5)), [2, 3, 4])
        self.assertEqual(list(my_range_gen(5, 2)), [])
        self.assertEqual(list(my_range_gen(5, 10)), [5, 6, 7, 8, 9])
