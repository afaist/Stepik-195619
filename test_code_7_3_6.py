from code_7_3_6 import is_palindrome
import unittest


class TestIsPalindrome(unittest.TestCase):
    def test_is_palindrome(self):
        self.assertTrue(is_palindrome("racecar"))
        self.assertTrue(is_palindrome("abba"))
        self.assertFalse(is_palindrome("hello"))
        self.assertFalse(is_palindrome("world"))
        self.assertTrue(is_palindrome("12321"))
