from code_5_7_11 import aggregation
import unittest


def get_add(x, y):
    return x + y


def get_max(x, y):
    return max(x, y)


def get_product(x, y):
    return x * y


class TestAggregation(unittest.TestCase):
    def test_add(self):
        self.assertEqual(aggregation(get_add, [1, 2]), 3)
        self.assertEqual(aggregation(get_add, [5, 2, 4, 3, 5]), 19)

    def test_max(self):
        self.assertEqual(aggregation(get_max, [1, 2, 3, 4, 5]), 5)
        self.assertEqual(aggregation(get_max, [5, 2, 4, 3, 5]), 5)
        self.assertEqual(aggregation(get_max, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 10)

    def test_product(self):
        self.assertEqual(aggregation(get_product, [1, 2]), 2)
        self.assertEqual(aggregation(get_product, [5, 2, 4, 3, 5]), 600)
