from code_3_7_15 import info_kwargs
import unittest
import io
from unittest.mock import patch


class TestInfoKwargs(unittest.TestCase):
    def setUp(self):
        self.captured_output = (
            io.StringIO()
        )  # Create a StringIO stream to capture output
        self.patched_stdout = patch("sys.stdout", self.captured_output)  # Patch stdout
        self.patched_stdout.start()

    def tearDown(self):
        self.patched_stdout.stop()

    def test_info_kwargs(self):
        info_kwargs(first_name="John", last_name="Doe", age=33)
        captured_output = self.captured_output.getvalue().strip()
        expected_output = "age = 33\nfirst_name = John\nlast_name = Doe"
        self.assertEqual(captured_output, expected_output)
        info_kwargs(c=43, b=32, a=32)
        captured_output = self.captured_output.getvalue().strip()
        expected_output += "\na = 32\nb = 32\nc = 43"
        self.assertEqual(captured_output, expected_output)
