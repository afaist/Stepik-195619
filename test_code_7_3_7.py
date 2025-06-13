from code_7_3_7 import get_arith_progression
import unittest


class TestGetArithProgression(unittest.TestCase):
    def test_get_arith_progression(self):
        self.assertEqual(get_arith_progression(1), 1)
        self.assertEqual(get_arith_progression(2), 8)
        self.assertEqual(get_arith_progression(3), 15)
