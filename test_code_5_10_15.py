from code_5_10_15 import filter_even, delete_short
import unittest


@filter_even
def concatenate(*args):
    print(args)
    result = ""
    for arg in args:
        result += str(arg)
    return result


@filter_even
@delete_short
def concatenate1(*args, **kwargs):
    result = ""
    for arg in args + tuple(kwargs.values()):
        result += str(arg)
    return result


class TestFilterEven(unittest.TestCase):
    def test_filter_even(self):
        self.assertEqual(
            concatenate("Ну", "Когда", "Уже", "Я", "Выучу", "Питон?"), "НуПитон?"
        )
        self.assertEqual(concatenate(1, 3, 5), "")
        self.assertEqual(concatenate(2, 4, 6), "246")

    def test_both(self):
        self.assertEqual(concatenate1(1, 2, 3, 4, 5, 6, a=7, b=8, c=9), "246")
        self.assertEqual(
            concatenate1(
                "Я", "хочу", "Выучить", "Питон", a="За", qwerty=10, c="Месяцев"
            ),
            "хочу10",
        )
