from code_7_2_11 import sum_recursive
import unittest


class TestSumRecursive(unittest.TestCase):
    def test_sum_recursive(self):
        self.assertEqual(sum_recursive([1, 2, 3]), 6)
        self.assertEqual(sum_recursive([1, 2, 3, 4]), 10)
        self.assertEqual(sum_recursive([1, 2, 3, 4, 5]), 15)
        self.assertEqual(sum_recursive([0]), 0)
        self.assertEqual(sum_recursive([]), 0)
