from code_7_2_18 import get_combin
import unittest


class TestGetCombin(unittest.TestCase):
    def test_get_combin(self):
        self.assertEqual(get_combin(5, 3), 10)
        self.assertEqual(get_combin(5, 2), 10)
        self.assertEqual(get_combin(1, 1), 1)
        self.assertEqual(get_combin(6, 3), 20)
        self.assertEqual(get_combin(7, 3), 35)
        self.assertEqual(get_combin(10, 7), 120)
