from code_7_4_3 import multu_recursive
import unittest


class TestMultuRecursive(unittest.TestCase):
    def test_multu_recursive(self):
        self.assertEqual(multu_recursive([5, 3]), 15)
        self.assertEqual(multu_recursive([1, 1]), 1)
        self.assertEqual(multu_recursive([0, 1]), 0)
        self.assertEqual(multu_recursive([0, 0]), 0)
        self.assertEqual(multu_recursive([1, 2, 3, 4, [[5]], [5]]), 600)
        self.assertEqual(multu_recursive([1, 2, 3, 4, [[5]], [5], 6, 7, 8, 9]), 1814400)
        self.assertEqual(
            multu_recursive(
                [1, 2, 3, 4, "A", [[5], "code_7_4_3"], [5], 6, "99", 7, 8, 9, 10, 11]
            ),
            199584000,
        )
