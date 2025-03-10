from code_5_6_8 import get_extensions
import unittest


class TestGetExtensions(unittest.TestCase):
    def test_get_extensions(self):
        self.assertEqual(get_extensions(["test.txt"]), ["txt"])
        self.assertEqual(
            get_extensions(["foo.txt", "bar.mp4", "python3"]), ["txt", "mp4", ""]
        )
        self.assertEqual(get_extensions([""]), [""])
