from code_5_10_13 import validate_all_args_str
import unittest


@validate_all_args_str
def concatenate(*args):
    result = ""
    for arg in args:
        result += arg
    return result


@validate_all_args_str
def concatenate1(**kwargs):
    result = ""
    for arg in kwargs.values():
        result += str(arg)
    return result


class TestValidateAllArgsStr(unittest.TestCase):
    def test_validate_all_args_str(self):
        self.assertEqual(concatenate("a", "b"), "ab")
        self.assertEqual(concatenate("a", "b", "c"), "abc")
        self.assertIsNone(concatenate("Home", 9, "month"))

    def test_validate_all_args_str2(self):
        self.assertEqual(
            concatenate1(a="Я", b="Выучу", c="Этот", d="Питон", e="!"),
            "ЯВыучуЭтотПитон!",
        )
