from code_5_8_7 import make_repeater
import unittest


class TestCode_5_8_7(unittest.TestCase):
    def test_make_repeater_3(self):
        repeater = make_repeater(3)
        self.assertEqual(repeater("Hello"), "HelloHelloHello")

    def test_make_repeater_5(self):
        repeater = make_repeater(5)
        self.assertEqual(repeater("Hello"), "HelloHelloHelloHelloHello")
