from code_5_6_10 import calculate
import unittest
import io
from unittest.mock import patch


class TestCalculate(unittest.TestCase):
    def setUp(self):
        self.captured_output = (
            io.StringIO()
        )  # Create a StringIO stream to capture output
        self.patched_stdout = patch("sys.stdout", self.captured_output)  # Patch stdout
        self.patched_stdout.start()

    def tearDown(self):
        self.patched_stdout.stop()

    def test_calculate(self):
        calculate(2, 5)
        captured = self.captured_output.getvalue().strip()
        expected = "7"
        self.assertEqual(captured, expected)
        calculate(2.2, 15, "a")
        expected += "\n17.2"
        self.assertEqual(self.captured_output.getvalue().strip(), expected)
