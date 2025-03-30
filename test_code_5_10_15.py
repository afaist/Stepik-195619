from code_5_10_15 import filter_even, delete_short
import unittest


@filter_even
def concatenate(*args):
    print(args)
    result = ""
    for arg in args:
        result += arg
    return result


class TestFilterEven(unittest.TestCase):
    def test_filter_even(self):
        self.assertEqual(
            concatenate("Ну", "Когда", "Уже", "Я", "Выучу", "Питон?"), "НуПитон?"
        )
        self.assertEqual(concatenate([1, 3, 5]), [])


print(concatenate("Ну", "Когда", "Уже", "Я", "Выучу", "Питон?"))
