from code_8_3_21 import check_password
import unittest


class TestCheckPassword(unittest.TestCase):
    def test_check_password(self):
        coro = check_password()
        self.assertIsNone(next(coro))
        self.assertFalse(coro.send("123456"))
        self.assertFalse(coro.send("qwerty"))
        self.assertFalse(coro.send("qwertyuiop"))
        self.assertFalse(coro.send("asdfghjkl"))
        self.assertFalse(coro.send("zxcvbnm"))
        self.assertFalse(coro.send("qwerty123!"))
        self.assertTrue(coro.send("QWERTY123!"))
        self.assertTrue(coro.send("Qwerty123@"))
        coro.close()
