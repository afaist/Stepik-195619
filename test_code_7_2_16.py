from code_7_2_16 import fibonacci
import unittest


class TestFibonacci(unittest.TestCase):
    def test_fibonacci(self):
        self.assertEqual(fibonacci(7), 13)
        self.assertEqual(fibonacci(5), 5)
        self.assertEqual(fibonacci(1), 1)
        self.assertEqual(fibonacci(10), 55)
