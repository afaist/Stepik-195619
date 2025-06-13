from code_7_3_3 import is_member
import unittest


class TestIsMember(unittest.TestCase):
    def test_is_member_for_numbers(self):
        self.assertTrue(is_member(1, [1, 2, 3]))
        self.assertFalse(is_member(4, [1, 2, 3]))
        self.assertFalse(is_member(1, []))
        self.assertTrue(is_member(1.0, [1, 2, 3]))  # float == int
        self.assertFalse(is_member(1.1, [1, 2, 3]))
        self.assertTrue(is_member(1, [1.0, 2.0, 3.0]))  # float == int

    def test_is_memeber_for_str(self):
        self.assertTrue(is_member("a", ["a", "b", "c"]))
        self.assertFalse(is_member("d", ["a", "b", "c"]))
        self.assertFalse(is_member("a", []))
        self.assertTrue(is_member("migthy", ["migth", "power", "migthy", "resistance"]))
        self.assertFalse(is_member("migthy", ["migth", "power", "migth"]))
