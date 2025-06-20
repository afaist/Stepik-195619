from code_8_1_9 import gen_odd
import unittest


class TestGenOdd(unittest.TestCase):
    def test_gen_odd(self):
        self.assertEqual(list(gen_odd(9)), [1, 3, 5, 7, 9])
        gen = gen_odd(9)
        self.assertEqual(next(gen), 1)
        self.assertEqual(next(gen), 3)
        self.assertEqual(next(gen), 5)
        self.assertEqual(next(gen), 7)
        self.assertEqual(next(gen), 9)
        self.assertRaises(StopIteration, next, gen)
