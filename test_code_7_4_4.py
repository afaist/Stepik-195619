from code_7_4_4 import get_max_recursive
import unittest


class TestGetMaxRecursive(unittest.TestCase):
    def test_get_max_recursive(self):
        self.assertEqual(get_max_recursive([1, 2, 3, 4, 5]), 5)
        self.assertEqual(get_max_recursive([1, 3, 5, 2, 4]), 5)
        self.assertEqual(get_max_recursive([5, 4, 3, 2, 1]), 5)

    def test_get_max_recursive_nested(self):
        self.assertEqual(get_max_recursive([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), 9)
        self.assertEqual(
            get_max_recursive([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]), 12
        )
        self.assertEqual(get_max_recursive([1, 2, 3, 4, [[5]], [5]]), 5)
