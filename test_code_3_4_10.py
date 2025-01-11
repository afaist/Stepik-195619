from code_3_4_10 import product
import unittest


class TestProduct(unittest.TestCase):
    def test_product(self):
        self.assertEqual(product([1, 2]), 2)
        self.assertEqual(product([1, 2, 3, 4]), 24)
        self.assertEqual(product([1, 2, 3, 4, 5]), 120)
        self.assertEqual(product([0, 1, 2, 3, 4, 5]), 0)
        self.assertEqual(product([1, 2, 3, 4, 5, 6], 2), 1440)
