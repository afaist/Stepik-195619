"""Test for code_7_1_18

Test for function print_to from code_7_1_18
"""

from code_7_1_18 import print_to
import unittest
import io
from unittest.mock import patch


class TestPrintTo(unittest.TestCase):
    """Test for print_to function"""

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_print_from_7(self, mock_stdout):
        print_to(7)
        self.assertEqual(mock_stdout.getvalue(), "1\n2\n3\n4\n5\n6\n7\n")

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_print_from_5(self, mock_stdout):
        print_to(5)
        self.assertEqual(mock_stdout.getvalue(), "1\n2\n3\n4\n5\n")
