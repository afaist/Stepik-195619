from code_3_2_6 import filter_long_words
import unittest


class TestFilterLongWords(unittest.TestCase):
    def test_filter_long_words(self):
        self.assertEqual(
            filter_long_words(["hello", "world", "this", "is", "a", "test"], 3),
            ["hello", "world", "this", "test"],
        )
        self.assertEqual(
            filter_long_words(["hello", "world", "this", "is", "a", "test"], 4),
            ["hello", "world"],
        )
