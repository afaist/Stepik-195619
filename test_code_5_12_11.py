from code_5_12_11 import convert_to
import unittest


class TestConvertTo(unittest.TestCase):
    def test_convert_to_int(self):
        @convert_to(int)
        def add_values(a, b):
            return a + b

        self.assertEqual(add_values(10, 20), 30)
        self.assertEqual(add_values("1", "2"), 12)
        self.assertEqual(add_values(1.0, 2.0), 3)
        self.assertEqual(add_values(1, 2.0), 3)
        self.assertEqual(add_values(1.0, 2), 3)
        self.assertIsInstance(add_values("1", "2"), int)

    def test_convert_to_str(self):
        @convert_to(str)
        def add_values(a, b):
            return a + b

        self.assertEqual(add_values(10, 20), "30")
        self.assertEqual(add_values("1", "2"), "12")
        self.assertEqual(add_values(1.0, 2.0), "3.0")
        self.assertIsInstance(add_values(1, 2), str)

    def test_convert_to_list(self):
        @convert_to(list)
        def add_values(a, b):
            return a + b

        self.assertEqual(add_values("1", "2"), ["1", "2"])
        self.assertIsInstance(add_values("hello", "world"), list)
