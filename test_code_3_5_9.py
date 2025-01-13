from code_3_5_9 import my_func
import unittest


class TestCode3_5_9(unittest.TestCase):
    def test_my_func(self):
        self.assertEqual(my_func([1, 2, 3], 3), [1, 2, 3, 1, 2, 3])
        a = [10, 20, 30]
        self.assertEqual(my_func(a, 3), [10, 20, 30, 1, 2, 3])
        self.assertEqual(a, [10, 20, 30])
