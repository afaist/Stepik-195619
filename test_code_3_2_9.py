from code_3_2_9 import find_longest_word_len
import unittest


class TestFindLongestWordLen(unittest.TestCase):
    def test_find_longest_word_len(self):
        self.assertEqual(
            find_longest_word_len(["apple", "banana", "cherry", "reserve"]), 7
        )
        self.assertEqual(
            find_longest_word_len(["apple", "banana", "ghostwriter", "cherry", "date"]),
            11,
        )
        self.assertNotEqual(
            find_longest_word_len(["brain", "candle", "rare", "shy"]), 8
        )
