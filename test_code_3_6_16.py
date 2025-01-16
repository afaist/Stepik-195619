from code_3_6_16 import print_goods
import io
import unittest
from unittest.mock import patch


class TestPrintGoods(unittest.TestCase):
    def setUp(self):
        self.captured_output = (
            io.StringIO()
        )  # Create a StringIO stream to capture output
        self.patched_stdout = patch("sys.stdout", self.captured_output)  # Patch stdout
        self.patched_stdout.start()

    def tearDown(self):
        self.patched_stdout.stop()

    def test_print_goods(self):
        print_goods("apple", "banana", "orange")
        captured_output = self.captured_output.getvalue().strip()
        expected_output = "1. apple\n2. banana\n3. orange"
        self.assertEqual(captured_output, expected_output)
        self.assertEqual(print_goods(1, True, "Грушечка", "", "Pineapple"), None)
        captured_output = self.captured_output.getvalue().strip()
        expected_output += "\n1. Грушечка\n2. Pineapple"
        self.assertEqual(print_goods([], {}, 1, 2), None)
        captured_output = self.captured_output.getvalue().strip()
        expected_output += "\nНет товаров"
        self.assertEqual(captured_output, expected_output)
