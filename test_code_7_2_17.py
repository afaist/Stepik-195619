from code_7_2_17 import tribonacci
import unittest


class TestTribonacci(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(tribonacci(0), 0)

    def test_one(self):
        self.assertEqual(tribonacci(1), 0)

    def test_two(self):
        self.assertEqual(tribonacci(2), 1)

    def test_three(self):
        self.assertEqual(tribonacci(3), 1)

    def test_four(self):
        self.assertEqual(tribonacci(4), 2)

    def test_five(self):
        self.assertEqual(tribonacci(5), 4)

    def test_six(self):
        self.assertEqual(tribonacci(6), 7)

    def test_seven(self):
        self.assertEqual(tribonacci(7), 13)

    def test_eight(self):
        self.assertEqual(tribonacci(8), 24)

    def test_nine(self):
        self.assertEqual(tribonacci(9), 44)

    def test_ten(self):
        self.assertEqual(tribonacci(10), 81)
