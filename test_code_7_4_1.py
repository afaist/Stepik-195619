from code_7_4_1 import get_sum
import unittest


class TestGetSum(unittest.TestCase):
    def test_get_sum_flat(self):
        self.assertEqual(get_sum([2, 2]), 4)
        self.assertEqual(get_sum([2, 3]), 5)
        self.assertEqual(get_sum([3, 4]), 7)

    def test_get_sum_nested(self):
        self.assertEqual(get_sum([[2, 2], [3, 4]]), 11)
        self.assertEqual(get_sum([[2, 3], [3, 4]]), 12)
        self.assertEqual(get_sum([[2, 3], [3, 4], [5, 6]]), 23)
        self.assertEqual(get_sum([[1, 2, 3], [4, [5, 6]], 7]), 28)
