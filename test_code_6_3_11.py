from code_6_3_11 import get_letters
import unittest


class TestGetLetter(unittest.TestCase):
    def test_get_letter(self):
        self.assertEqual(get_letters("a"), [("A", "a")])
        self.assertEqual(get_letters("b"), [("B", "b")])
        self.assertEqual(get_letters("z"), [("Z", "z")])
        self.assertEqual(get_letters("abc"), [("A", "a"), ("B", "b"), ("C", "c")])
        self.assertEqual(
            get_letters("MeSsi"),
            [("M", "m"), ("E", "e"), ("S", "s"), ("S", "s"), ("I", "i")],
        )
