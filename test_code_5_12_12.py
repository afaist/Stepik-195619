from code_5_12_12 import validate_all_args
import unittest
from unittest.mock import patch, call


class TestValidateAllArgs(unittest.TestCase):
    @patch("builtins.print")
    def test_print_args_kwargs_str(self, mock_print):
        @validate_all_args(str)
        def print_args_kwargs(*args, **kwargs):
            for i, value in enumerate(args):
                print(i, value)
            for k, v in kwargs.items():
                print(f"{k} = {v}")

        self.assertIsNone(print_args_kwargs(1, 2, 3, b=300, w=40, t=50, a=100))
        self.assertEqual(
            mock_print.mock_calls,
            [call("Все аргументы должны принадлежать типу <class 'str'>")],
        )
        mock_print.reset_mock()

    @patch("builtins.print")
    def test_print_args_kwargs_int(self, mock_print):
        @validate_all_args(int)
        def print_args_kwargs(*args, **kwargs):
            for i, value in enumerate(args):
                print(i, value)
            for k, v in kwargs.items():
                print(f"{k} = {v}")

        self.assertIsNone(print_args_kwargs(1, 2, 3, b=300, w=40, t=50, a=100))
        self.assertEqual(
            mock_print.mock_calls,
            [
                call(0, 1),
                call(1, 2),
                call(2, 3),
                call("b = 300"),
                call("w = 40"),
                call("t = 50"),
                call("a = 100"),
            ],
        )
        mock_print.reset_mock()

    @patch("builtins.print")
    def test_print_args_kwargs_list(self, mock_print):
        @validate_all_args(list)
        def print_args_kwargs(*args, **kwargs):
            for i, value in enumerate(args):
                print(i, value)
            for k, v in kwargs.items():
                print(f"{k} = {v}")

        self.assertIsNone(
            print_args_kwargs([1, 2, 3], b=[300, 400], w=[40, 50], a=[100, 200])
        )
        self.assertEqual(
            mock_print.mock_calls,
            [
                call(0, [1, 2, 3]),
                call("b = [300, 400]"),
                call("w = [40, 50]"),
                call("a = [100, 200]"),
            ],
        )
