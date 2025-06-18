from code_7_4_7 import find_level_element
import unittest


class TestFindLevelElement(unittest.TestCase):
    def test_find_level_element(self):
        self.assertEqual(find_level_element(5, [1, 2, 3, 4, 5]), 1)
        self.assertEqual(find_level_element(5, [1, 2, 3, 4, [5]]), 2)
        self.assertEqual(find_level_element(1, [[[1]], 2, 3, 4, 5]), 3)
        self.assertEqual(find_level_element(1, [2, 3, 4, 5]), -1)
        self.assertEqual(find_level_element(5, [1, 2, 3, 4, [[5]], [5]]), 3)
        self.assertEqual(find_level_element(5, [1, 2, 3, 4, [[8], [5]]]), 3)
        self.assertEqual(find_level_element(5, [1, 2, 3, 4, [8], [5]]), 2)
