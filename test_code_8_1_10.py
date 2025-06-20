from code_8_1_10 import alphabet
import unittest


class TestAlphabet(unittest.TestCase):
    def test_alphabet(self):
        g = alphabet()
        self.assertEqual(next(g), ("a", "apple"))
        self.assertEqual(next(g), ("b", "banana"))
        self.assertEqual(next(g), ("c", "cat"))
        self.assertEqual(next(g), ("d", "dog"))
        self.assertRaises(StopIteration, next, g)
