from code_8_1_13 import gen_arithmetic_progression
import unittest


class TestGenArithmeticProgression(unittest.TestCase):
    def test_gen_arithmetic_progression(self):
        progression = gen_arithmetic_progression(5, 7)
        self.assertEqual(next(progression), 5)
        self.assertEqual(next(progression), 12)
        self.assertEqual(next(progression), 19)
        self.assertEqual(next(progression), 26)
        self.assertEqual(next(progression), 33)
