from code_7_2_9 import summa
import unittest


class TestSumma(unittest.TestCase):
    def test_summa(self):
        self.assertEqual(summa(3), 6)
        self.assertEqual(summa(4), 10)
        self.assertEqual(summa(10), 55)
        self.assertEqual(summa(11), 66)
        self.assertEqual(summa(13), 91)
        self.assertEqual(summa(34), 595)
