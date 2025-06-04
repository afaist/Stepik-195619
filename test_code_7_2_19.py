from code_7_2_19 import ackermann
import unittest


class TestAckerman(unittest.TestCase):
    def test_ackerman(self):
        self.assertEqual(ackermann(1, 5), 7)
        self.assertEqual(ackermann(3, 3), 61)
        self.assertEqual(ackermann(2, 4), 11)
        self.assertEqual(ackermann(3, 2), 29)
