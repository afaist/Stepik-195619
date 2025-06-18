from code_7_4_5 import flatten
import unittest


class TestFlatten(unittest.TestCase):
    def test_flatten(self):
        self.assertEqual(flatten([1, 2, 3, [4, 5]]), [1, 2, 3, 4, 5])
        self.assertEqual(flatten([1, [2, [3, 4], 5]]), [1, 2, 3, 4, 5])
        self.assertEqual(flatten([[1], [2], [3], [4], [5]]), [1, 2, 3, 4, 5])
        self.assertEqual(flatten([[[1]]]), [1])
        self.assertEqual(flatten([1, [2, [3, [4, [5, [6]]]]]]), [1, 2, 3, 4, 5, 6])
        self.assertEqual(flatten([[[[9]]], [1, 2], [[8]]]), [9, 1, 2, 8])
