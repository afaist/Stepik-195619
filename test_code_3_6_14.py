from code_3_6_14 import check_sum
import io
import unittest
from unittest.mock import patch


class TestChecSum(unittest.TestCase):
    def setUp(self):
        self.captured_output = (
            io.StringIO()
        )  # Create a StringIO stream to capture output
        self.patched_stdout = patch("sys.stdout", self.captured_output)  # Patch stdout
        self.patched_stdout.start()

    def tearDown(self):
        self.patched_stdout.stop()

    def test_1(self):
        self.assertEqual(check_sum(4, 9), None)
        captured_output = self.captured_output.getvalue().strip()
        expected_output = "not enough"  # Replace with your expected output
        self.assertEqual(captured_output, expected_output)
        self.assertEqual(check_sum(4, 10, 10, 10, 10, 9), None)  #
        captured_output = self.captured_output.getvalue().strip()
        expected_output += "\nverification passed"
        self.assertEqual(captured_output, expected_output)
