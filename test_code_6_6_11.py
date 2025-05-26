from code_6_6_11 import find_different_indexes
import unittest


class TestFindDifferentIndexes(unittest.TestCase):
    def test_find_different_indexes(self):
        self.assertEqual(find_different_indexes("abcd", "artd"), [1, 2])
        self.assertEqual(find_different_indexes("abc", "abc"), [])
        self.assertEqual(find_different_indexes("abc", "xyz"), [0, 1, 2])
        self.assertEqual(
            find_different_indexes("abracadabra", "uzrucuduzru"), [0, 1, 3, 5, 7, 8, 10]
        )
