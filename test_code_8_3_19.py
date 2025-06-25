from code_8_3_19 import is_palindrome
import unittest


class TestIsPalindrome(unittest.TestCase):
    def test_is_palindrome(self):
        coro = is_palindrome()
        self.assertFalse(next(coro))
        self.assertTrue(coro.send(1771))
        self.assertFalse(coro.send(1772))
        self.assertTrue(coro.send(121))
        self.assertTrue(coro.send(0))
        coro.close()
