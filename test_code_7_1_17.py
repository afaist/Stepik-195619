from code_7_1_17 import print_from
import unittest
import io
from unittest.mock import patch


class TestPrintFrom(unittest.TestCase):
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_print_from_7(self, mock_stdout):
        print_from(7)
        self.assertEqual(mock_stdout.getvalue(), "7\n6\n5\n4\n3\n2\n1\n")

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_print_from_5(self, mock_stdout):
        print_from(5)
        self.assertEqual(mock_stdout.getvalue(), "5\n4\n3\n2\n1\n")
