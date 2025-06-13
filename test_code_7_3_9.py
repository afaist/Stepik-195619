from code_7_3_9 import quick_power
import unittest
import io
from unittest.mock import patch


class TestQuickPower(unittest.TestCase):
    def test_quick_power(self):
        self.assertEqual(quick_power(2, 3), 8)
        self.assertEqual(quick_power(2, 4), 16)
        self.assertEqual(quick_power(2, 0), 1)
        self.assertEqual(quick_power(2, 24), 16777216)
        self.assertEqual(quick_power(2, 30), 1073741824)
        self.assertEqual(quick_power(1, 1000000), 1)

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_quick_power_out(self, mock_stdout):
        quick_power(3, 4)
        self.assertEqual(
            mock_stdout.getvalue(),
            "State: a=3, n=4\nState: a=3, n=2\nState: a=3, n=1\nState: a=3, n=0\n",
        )
        mock_stdout.close()
