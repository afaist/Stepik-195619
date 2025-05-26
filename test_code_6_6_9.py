from code_6_6_9 import even_items
import unittest


class TestEvenItems(unittest.TestCase):
    def test_even_items(self):
        self.assertEqual(even_items([1, 2, 3, 4, 5]), [2, 4])
        self.assertEqual(even_items([1, 3, 5]), [3])
        self.assertEqual(even_items([2, 4, 6, 8]), [4, 8])
        self.assertEqual(even_items([1, 3, 5, 7, 9]), [3, 7])
