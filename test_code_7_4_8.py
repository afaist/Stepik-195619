from code_7_4_8 import reversed_recursive
import unittest


class TestReversedRecursive(unittest.TestCase):
    def test_reversed_recursive(self):
        self.assertEqual(reversed_recursive([1, 2, 3]), [3, 2, 1])
        self.assertEqual(reversed_recursive([1, [2, 3], 4]), [4, [3, 2], 1])
        self.assertEqual(
            reversed_recursive([[1, 2, 3], [4, 5], [6, 7, 8]]),
            [[8, 7, 6], [5, 4], [3, 2, 1]],
        )
        self.assertEqual(reversed_recursive([[1, 2, 3]]), [[3, 2, 1]])
        self.assertEqual(
            reversed_recursive([[1, 2, 3], [4, [5, [6]]], 7]),
            [7, [[[6], 5], 4], [3, 2, 1]],
        )
