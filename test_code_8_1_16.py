from code_8_1_16 import gen_factorial
import unittest


class TestGenFactorial(unittest.TestCase):
    def test_gen_factorial(self):
        number = gen_factorial()
        self.assertEqual(next(number), 1)
        self.assertEqual(next(number), 2)
        self.assertEqual(next(number), 6)
        self.assertEqual(next(number), 24)
        self.assertEqual(next(number), 120)
        self.assertEqual(next(number), 720)
        self.assertEqual(next(number), 5040)
        self.assertEqual(next(number), 40320)
        self.assertEqual(next(number), 362880)
        self.assertEqual(next(number), 3628800)
