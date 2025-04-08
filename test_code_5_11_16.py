from code_5_11_16 import cache_result
import unittest
from unittest.mock import patch, call


class TestCacheResult(unittest.TestCase):
    @patch("builtins.print")
    def test_multiply(self, mocked_print):
        @cache_result
        def multiply(a, b):
            return a * b

        self.assertEqual(multiply(4, 5), 20)
        self.assertEqual(multiply(4, 5), 20)
        self.assertEqual(
            mocked_print.mock_calls, [call("[FROM CACHE] Вызов multiply = 20")]
        )
        mocked_print.reset_mock()
        self.assertEqual(multiply(5, 8), 40)
        self.assertEqual(multiply(5, 8), 40)
        self.assertEqual(
            mocked_print.mock_calls, [call("[FROM CACHE] Вызов multiply = 40")]
        )
        mocked_print.reset_mock()

    @patch("builtins.print")
    def test_add(self, mocked_print):
        @cache_result
        def add(a, b):
            return a + b

        self.assertEqual(add(4, 5), 9)
        self.assertEqual(add(4, 5), 9)
        self.assertEqual(mocked_print.mock_calls, [call("[FROM CACHE] Вызов add = 9")])
        mocked_print.reset_mock()
        self.assertEqual(add(5, 8), 13)
        self.assertEqual(add(5, 8), 13)
        self.assertEqual(mocked_print.mock_calls, [call("[FROM CACHE] Вызов add = 13")])
        mocked_print.reset_mock()
