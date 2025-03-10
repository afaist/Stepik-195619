from code_5_5_14 import count_strings
import unittest


class TestCountStrings(unittest.TestCase):
    def test_count_strings(self):
        self.assertEqual(count_strings(1, 2, "hello", True, "t"), 2)
        self.assertEqual(count_strings(1, 2, "hello", True, "t", "world"), 3)
        self.assertEqual(count_strings(1, 2, "hello", True, "t", "world", "1"), 4)
        self.assertNotEqual(count_strings(1, 2, 3), 1)
