from code_8_1_11 import my_range_gen
import unittest


class TestMyRangeGen(unittest.TestCase):
    def test_my_range_gen(self):
        result = list(my_range_gen(10))
        self.assertEqual(result, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_my_range_gen_2(self):
        result = list(my_range_gen(0))
        self.assertEqual(result, [])

    def test_my_range_gen_3(self):
        result = list(my_range_gen(-10))
        self.assertEqual(result, [])

    def test_my_range_gen_4(self):
        result = list(my_range_gen(1))
        self.assertEqual(result, [0])

    def test_my_range_gen_5(self):
        result = my_range_gen(3)
        self.assertEqual(next(result), 0)
        self.assertEqual(next(result), 1)
        self.assertEqual(next(result), 2)
        self.assertRaises(StopIteration, next, result)
