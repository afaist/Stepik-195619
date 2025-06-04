from code_7_2_10 import find_min
import unittest


class TestFindMin(unittest.TestCase):
    def test_find_min(self):
        self.assertEqual(find_min([1, 2, 3, 4, 5]), 1)
        self.assertEqual(find_min([5, 4, 3, 2, 1]), 1)
        self.assertEqual(find_min([5, 4, 3, 2, 1, 2, 3, 4, 5]), 1)
        self.assertEqual(find_min([2, 3, 4, 1, 5]), 1)
        self.assertEqual(find_min([-230, 101, 323, -200, 17, -5, 10, -22]), -230)
