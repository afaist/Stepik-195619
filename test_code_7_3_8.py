from code_7_3_8 import get_arith_progression
import unittest


class TestGetArithProgression(unittest.TestCase):
    def test_get_arith_progression(self):
        self.assertEqual(get_arith_progression(4, 2, 3), 8)
        self.assertEqual(get_arith_progression(3, 10, 2), 13)
        self.assertEqual(get_arith_progression(3, 10, 3), 23)
