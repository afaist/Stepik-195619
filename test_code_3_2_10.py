from code_3_2_10 import register_check
import unittest


class TestRegisterCheck(unittest.TestCase):
    def test_register_check_two(self):
        people = {"Igor": "yes", "Stas": "no", "Peter": "no", "Mary": "yes"}
        self.assertEqual(register_check(people), 2)

    def test_register_check_five(self):
        people = {
            "Igor": "yes",
            "Vasya": "yes",
            "Peter": "yes",
            "Mary": "no",
            "Alex": "yes",
            "Marina": "yes",
        }
        self.assertEqual(register_check(people), 5)

    def test_register_check_zero(self):
        people = {}
        self.assertEqual(register_check(people), 0)
        people = {
            "Igor": "yes",
            "Vasya": "yes",
            "Peter": "yes",
            "Mary": "no",
            "Alex": "yes",
            "Marina": "yes",
        }
        self.assertNotEqual(register_check(people), 0)
