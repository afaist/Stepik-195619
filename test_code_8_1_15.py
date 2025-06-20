from code_8_1_15 import gen_factorial
import unittest


class TestGenFactorial(unittest.TestCase):
    def test_gen_factorial(self):
        self.assertEqual(list(gen_factorial(5)), [1, 2, 6, 24, 120])
        self.assertEqual(
            list(gen_factorial(10)),
            [1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800],
        )
        self.assertEqual(list(gen_factorial(0)), [])
        self.assertEqual(list(gen_factorial(-1)), [])
