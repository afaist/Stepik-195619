from code_5_12_8 import limit_query
import unittest
from unittest.mock import patch, call


class TestLimitQuery(unittest.TestCase):
    @patch("builtins.print")
    def test_add_3(self, mocked_print):
        @limit_query(limit=3)
        def add(a: int, b: int):
            return a + b

        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(3, 4), 7)
        self.assertEqual(add(4, 5), None)
        self.assertEqual(mocked_print.call_count, 1)
        self.assertEqual(
            mocked_print.mock_calls,
            [call("Лимит вызовов закончен, все 3 попытки израсходованы")],
        )
        mocked_print.reset_mock()
