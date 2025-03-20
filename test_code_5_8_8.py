from code_5_8_8 import create_accumulator
import unittest


class TestCreateAccumulator(unittest.TestCase):
    def setUp(self):
        self.summator_1 = create_accumulator()
        self.summator_2 = create_accumulator()

    def test_create_accumulator(self):
        self.assertEqual(self.summator_1(1), 1)
        self.assertEqual(self.summator_1(5), 6)
        self.assertEqual(self.summator_1(2), 8)
        self.assertEqual(self.summator_2(3), 3)
        self.assertEqual(self.summator_2(4), 7)
