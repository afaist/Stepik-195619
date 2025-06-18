from code_7_4_6 import is_member
import unittest


class TestIsMember(unittest.TestCase):
    def test_is_member(self):
        self.assertTrue(is_member(3, [1, 2, 3, 4, 5]))
        self.assertFalse(is_member(6, [1, 2, 3, 4, 5]))

    def test_is_member_nested(self):
        self.assertTrue(is_member(3, [[1, 2, 3, 4, 5]]))
        self.assertFalse(is_member(6, [[1, 2, 3, 4, 5]]))
        self.assertTrue(is_member(3, [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]))
        self.assertFalse(is_member(8, [[1, 2, 3], [4, [5, 6]], 7]))
        self.assertTrue(
            is_member(9, [1, 2, 3, 4, 5, [6, 7, 8, [9, 1, [2, [3], 4], 5, 6]]])
        )
