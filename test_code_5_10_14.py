from code_5_10_14 import validate_all_kwargs_int_pos
import unittest


@validate_all_kwargs_int_pos
def concatenate(*args, **kwargs):
    result = ""
    for arg in args + tuple(kwargs.values()):
        result += str(arg)
    return result


class TestValidateAllKwargsIntPos(unittest.TestCase):
    def test_valid_args(self):
        self.assertIsNone(concatenate(1, 2, 3, a="i", b="Love", c="Python"))
        self.assertEqual(concatenate(a=10, b=20, c=50), "102050")
