from code_5_11_15 import check_count_args
import unittest
from unittest.mock import patch, call
from functools import reduce


class TestCheckCountArgs(unittest.TestCase):
    @patch("builtins.print")
    def test_add_numbers(self, mocked_print):
        @check_count_args
        def add_numbers(x, y):
            """Return sum of x and y"""
            return x + y

        self.assertEqual(add_numbers(5, 6), 11)
        self.assertEqual(add_numbers(5, 6, 7), None)
        self.assertEqual(mocked_print.mock_calls, [call("Too many arguments")])
        mocked_print.reset_mock()
        self.assertEqual(add_numbers(5), None)
        self.assertEqual(mocked_print.mock_calls, [call("Not enough arguments")])

    @patch("builtins.print")
    def test_multiply(self, mocked_print):
        @check_count_args
        def multiply(*args):
            """Return the product of all arguments"""
            return reduce(lambda x, y: x * y, args)

        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(2, 3, 4), None)
        self.assertEqual(mocked_print.mock_calls, [call("Too many arguments")])
        mocked_print.reset_mock()
        self.assertEqual(multiply(3), None)
        self.assertEqual(mocked_print.mock_calls, [call("Not enough arguments")])

    @patch("builtins.print")
    def test_concatenate(self, mocked_print):
        @check_count_args
        def concatenate(**kwargs):
            """Return a string that concatenates all values in kwargs"""
            return "".join(kwargs.values())

        self.assertEqual(concatenate(a="a", b="b"), "ab")
        self.assertEqual(concatenate(a="a", b="b", c="c"), None)
        self.assertEqual(mocked_print.mock_calls, [call("Too many arguments")])
        mocked_print.reset_mock()
        self.assertEqual(concatenate(a="a"), None)
        self.assertEqual(mocked_print.mock_calls, [call("Not enough arguments")])
