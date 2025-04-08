from code_5_11_10 import add_args
import unittest


class TestAddArgs(unittest.TestCase):
    def test_concatenate(self):
        @add_args
        def concatenate(*args):
            return ", ".join(args)

        self.assertEqual(concatenate("Hello", "world"), "begin, Hello, world, end")
        self.assertEqual(
            concatenate("Hello", "world", "!", "Good", "morning"),
            "begin, Hello, world, !, Good, morning, end",
        )

    def test_find_max_word(self):
        @add_args
        def find_max_word(*args):
            return max(args, key=len)

        self.assertEqual(find_max_word("Hy", "worm"), "begin")
        self.assertEqual(
            find_max_word("Hello", "world", "!", "Good", "morning"), "morning"
        )
