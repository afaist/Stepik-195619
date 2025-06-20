from code_8_1_20 import my_range_gen
import unittest


class TestMyRangeGen(unittest.TestCase):
    def test_my_range_gen(self):
        result = list(my_range_gen(1, 10, 2))
        expected = [1, 3, 5, 7, 9]
        self.assertEqual(result, expected)
        self.assertEqual(list(my_range_gen(5)), [0, 1, 2, 3, 4])
        self.assertEqual(list(my_range_gen(2, 10, 2)), [2, 4, 6, 8])
        self.assertEqual(list(my_range_gen(5)), [0, 1, 2, 3, 4])
        self.assertEqual(list(my_range_gen(5, 1, -1)), [5, 4, 3, 2])
        self.assertEqual(list(my_range_gen(5, 0, -1)), [5, 4, 3, 2, 1])
        self.assertEqual(list(my_range_gen(20, 40, 0)), [])
        self.assertEqual(
            list(my_range_gen(10, 20)), [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
        )
        self.assertEqual(list(my_range_gen(20, 10, 2)), [])
