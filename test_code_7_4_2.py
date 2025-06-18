from code_7_4_2 import sum_recursive
import unittest


class TestSumRecursive(unittest.TestCase):
    def test_sum_recursive(self):
        self.assertEqual(sum_recursive([1, 2, 3]), 6)
        self.assertEqual(sum_recursive([1, [2, 3, 4], 5]), 15)
        self.assertEqual(sum_recursive([1, [2, [3, 4, 5], 6], 7]), 28)
