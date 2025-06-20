from code_8_1_14 import gen_fibonacci_numbers
import unittest


class TestGenFibonacciNumbers(unittest.TestCase):
    def test_gen_fibonacci_numbers(self):
        self.assertEqual(
            list(gen_fibonacci_numbers(10)), [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
        )
        self.assertEqual(list(gen_fibonacci_numbers(0)), [])
        self.assertEqual(list(gen_fibonacci_numbers(-10)), [])
        self.assertEqual(list(gen_fibonacci_numbers(1)), [1])
        self.assertEqual(list(gen_fibonacci_numbers(2)), [1, 1])
