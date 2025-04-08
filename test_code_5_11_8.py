from code_5_11_8 import limit_query
import unittest


@limit_query
def add(a: int, b: int):
    return a + b


class TestLimintQuery(unittest.TestCase):
    def countTestCases(self) -> int:
        return super().countTestCases()

    def test_limit(self):
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(2, 2), 4)
        self.assertEqual(add(3, 2), 5)
        self.assertIsNone(add(5, 8))
