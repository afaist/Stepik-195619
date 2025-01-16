from code_3_6_15 import is_only_one_positive
import unittest


class test_is_only_one_positivei(unittest.TestCase):
    def test_is_only_one_positive(self):
        self.assertEqual(is_only_one_positive(1, 2, 3, 4, 5), False)
        self.assertEqual(is_only_one_positive(-1, -2, 3, -4, -5), True)
        self.assertEqual(is_only_one_positive(1, 2, 3, 4, -5), False)
        self.assertEqual(is_only_one_positive(-1, -2, -3, -4, 0), False)
