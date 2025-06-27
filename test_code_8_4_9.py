from code_8_4_9 import alphabet
import unittest


class TestAlphabet(unittest.TestCase):
    def test_alphabet(self):
        coro = alphabet()
        next(coro)
        self.assertEqual(coro.send("a"), "apple")
        self.assertEqual(coro.send("b"), "banana")
        self.assertEqual(coro.send("c"), "cat")
        self.assertEqual(coro.throw(KeyError), "default")
        self.assertEqual(coro.send("d"), "dog")
        self.assertEqual(coro.send("1"), "default")
        self.assertEqual(coro.send("e"), "elephant")
        coro.close()

    def test_alphabet1(self):
        coro = alphabet()
        next(coro)
        self.assertEqual(coro.send("apple"), "default")
        self.assertEqual(coro.send("banana"), "default")
        self.assertEqual(coro.throw(KeyError), "default")
        self.assertEqual(coro.send("dog"), "default")
        self.assertEqual(coro.send("d"), "dog")
