from code_5_7_5 import apply
import unittest


def square(num):
    return num * num


def repeater(value, n=5):
    return str(value) * n


class TestApply(unittest.TestCase):
    def test_apply(self):
        self.assertEqual(apply(square, [5, 6, 7]), [5 * 5, 6 * 6, 7 * 7])
        self.assertEqual(
            apply(repeater, ["Hi", True, 0, [1, 2]]),
            [
                "HiHiHiHiHi",
                "TrueTrueTrueTrueTrue",
                "00000",
                "[1, 2][1, 2][1, 2][1, 2][1, 2]",
            ],
        )
        self.assertEqual(
            apply(repeater, "hello"), ["hhhhh", "eeeee", "lllll", "lllll", "ooooo"]
        )
