from code_5_7_6 import compute
import unittest


def square(num):
    return num**2


def inc(num):
    return num + 1


def dec(num):
    return num - 1


def repeater(value, n=10):
    return str(value) * n


class TestCompute(unittest.TestCase):
    def test_compute(self):
        self.assertEqual(compute([square, inc, dec, inc], 10), [100, 11, 9, 11])
        self.assertEqual(
            compute([inc, dec, square], 10, 20, 30, 40),
            [11, 21, 31, 41, 9, 19, 29, 39, 100, 400, 900, 1600],
        )
        self.assertEqual(
            compute([repeater, dec, inc, square], 5, 7, 0, True),
            [
                "5555555555",
                "7777777777",
                "0000000000",
                "TrueTrueTrueTrueTrueTrueTrueTrueTrueTrue",
                4,
                6,
                -1,
                0,
                6,
                8,
                1,
                2,
                25,
                49,
                0,
                1,
            ],
        )
