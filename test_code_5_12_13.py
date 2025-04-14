from code_5_12_13 import compose
import unittest


def double_it(a):
    return a * 2


def increment(a):
    return a + 1


class TestCompose(unittest.TestCase):
    def test_two_functions(self):
        @compose(double_it, increment)
        def get_sum(*args):
            return sum(args)

        self.assertEqual(get_sum(2), 5)
        self.assertEqual(get_sum(2, 3), 11)
        self.assertEqual(get_sum(2, 3, 4), 19)
        self.assertEqual(get_sum(5, 15, 25), 91)

    def test_three_functions(self):
        @compose(increment, double_it, increment)
        def get_sum(*args):
            return sum(args)

        self.assertEqual(get_sum(2), 7)
        self.assertEqual(get_sum(2, 3), 13)
