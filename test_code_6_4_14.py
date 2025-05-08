from code_6_4_14 import filter_words
import unittest


class TestFilterWords(unittest.TestCase):
    def test_filter_words(self):
        self.assertEqual(
            filter_words(["hello", "world", "python", "programming", "four"]),
            ["four"],
        )
        self.assertEqual(filter_words(["one", "two", "three", "four"]), ["four"])
        self.assertEqual(
            filter_words(
                [
                    "One",
                    "Two",
                    "Three",
                    "Four",
                    "Five",
                    "Six",
                    "Seven",
                    "Eight",
                    "Nine",
                    "Ten",
                    "Eleven",
                    "Twelve",
                ]
            ),
            ["Four", "Five", "Six", "Seven", "Nine"],
        )
