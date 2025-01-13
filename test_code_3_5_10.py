from code_3_5_10 import lstrip
import unittest


class TestLstrip(unittest.TestCase):
    def test(self):
        data = [0, 0, 1, 0, 2, 3]
        self.assertEqual(lstrip(data, 0), None)
        self.assertEqual(data, [1, 0, 2, 3])

        data = [1, 1, 1, 1, 0, 1, 0, 2, 3]
        lstrip(data, 1)
        self.assertEqual(data, [0, 1, 0, 2, 3])

    def testZero(self):
        data = [0, 0, 0, 0, 0, 0, 0]
        self.assertEqual(lstrip(data, 0), None)
        self.assertEqual(data, [])
