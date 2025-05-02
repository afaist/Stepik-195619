from code_6_3_9 import increase_3
import unittest


class TestIncrease_3(unittest.TestCase):
    def test_int(self):
        self.assertEqual(
            increase_3([16, -1, 8, 6, -5, -9, 22, 26, 7, -10]),
            (48, -3, 24, 18, -15, -27, 66, 78, 21, -30),
        )
        self.assertTupleEqual(
            increase_3([1238, 16, -53, -59, 10]), (3714, 48, -159, -177, 30)
        )
