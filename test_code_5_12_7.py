from code_5_12_7 import multiply_result_by
import unittest


class TestMultiplyResultBy(unittest.TestCase):
    def test_add(self):
        @multiply_result_by(2)
        def add(a, b):
            return a + b

        self.assertEqual(add(2, 3), 10)
        self.assertEqual(add(4, 5), 18)

    def test_sub(self):
        @multiply_result_by(2)
        def sub(a, b):
            return a - b

        self.assertEqual(sub(2, 3), -2)
        self.assertEqual(sub(4, 5), -2)

    def test_add_and_multiply(self):
        @multiply_result_by(3)
        @multiply_result_by(4)
        def add(a, b):
            return a + b

        self.assertEqual(add(2, 3), 60)
        self.assertEqual(add(5, 5), 120)
