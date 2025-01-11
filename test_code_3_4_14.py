from code_3_4_14 import create_student, add_mark
import io
import unittest
from unittest.mock import patch


class TestConsoleOutput(unittest.TestCase):
    def setUp(self):
        self.captured_output = (
            io.StringIO()
        )  # Create a StringIO stream to capture output
        self.patched_stdout = patch("sys.stdout", self.captured_output)  # Patch stdout
        self.patched_stdout.start()

    def tearDown(self):
        self.patched_stdout.stop()

    def test_create_student(self):
        ivan = create_student("Ivan", 15)
        print(ivan)
        captured_output = self.captured_output.getvalue().strip()  # Get captured output
        expected_output = "{'name': 'Ivan', 'age': 15, 'marks': []}"  # Replace with your expected output
        self.assertEqual(captured_output, expected_output)
        anatoliy = create_student("Anatoliy", 16, [5, 5, 5, 5, 5, 5, 5, 5, 5, 5])
        print(anatoliy)
        captured_output = self.captured_output.getvalue().strip()
        expected_output += (
            "\n{'name': 'Anatoliy', 'age': 16, 'marks': [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]}"
        )
        self.assertEqual(captured_output, expected_output)
        add_mark(ivan, 5)
        print(ivan)
        captured_output = self.captured_output.getvalue().strip()
        expected_output += "\n{'name': 'Ivan', 'age': 15, 'marks': [5]}"
