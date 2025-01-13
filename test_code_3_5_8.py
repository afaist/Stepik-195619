from code_3_5_8 import words_length
import unittest


class TestWordsLength(unittest.TestCase):
    def test_words_length(self):
        words = ["Hello", "world!"]
        words_length(words)
        self.assertEqual(words, [5, 6])

    def test_words_length_empty(self):
        words = []
        words_length(words)
        self.assertEqual(words, [])

    def test_return_value(self):
        words = ["Hello", "world!"]
        self.assertEqual(words_length(words), None)
