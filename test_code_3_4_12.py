from code_3_4_12 import show_list
import io
import unittest
from unittest.mock import patch

shopping_list = {"Bread": 13, "Potato": 5, "Milk": 2, "Orange": 5}


class TestConsoleOutput(unittest.TestCase):
    def setUp(self):
        self.captured_output = (
            io.StringIO()
        )  # Create a StringIO stream to capture output
        self.patched_stdout = patch("sys.stdout", self.captured_output)  # Patch stdout
        self.patched_stdout.start()

    def tearDown(self):
        self.patched_stdout.stop()

    def test_console_print(self):
        show_list()  # Call the function with print statements
        captured_output = self.captured_output.getvalue().strip()  # Get captured output
        expected_output = (
            "13xBread\n5xPotato\n2xMilk\n5xOrange"  # Replace with your expected output
        )
        self.assertEqual(captured_output, expected_output)
        show_list(False)
        captured_output = self.captured_output.getvalue().strip()
        expected_output = (
            "13xBread\n5xPotato\n2xMilk\n5xOrange\nBread\nPotato\nMilk\nOrange"
        )
        self.assertEqual(captured_output, expected_output)
