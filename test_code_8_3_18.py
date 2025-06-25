from code_8_3_18 import alphabet
import unittest


class TestAlphabet(unittest.TestCase):
    def test_alphabet(self):
        coro = alphabet()
        self.assertEqual(next(coro), None)
        self.assertEqual(coro.send("a"), "apple")
        self.assertEqual(coro.send("b"), "banana")
        self.assertEqual(coro.send("c"), "cat")
        coro.close()

    def test_alphabet_2(self):
        coro = alphabet()
        self.assertEqual(next(coro), None)
        self.assertEqual(coro.send("d"), "dog")
        self.assertEqual(coro.send("e"), "elephant")
        self.assertEqual(coro.send("f"), "fox")
        coro.close()
