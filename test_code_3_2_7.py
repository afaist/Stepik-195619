from code_3_2_7 import is_member
import unittest


class TestCode_3_2_7(unittest.TestCase):
    def test_is_member(self):
        assert is_member("e", ["a", "e", "i", "o", "u"])
        assert not is_member("b", ["a", "e", "i", "o", "u"])
        assert is_member("a", ["a", "e", "i", "o", "u"])
        assert not is_member("x", ["a", "e", "i", "o", "u"])
