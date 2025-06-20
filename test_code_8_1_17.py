from code_8_1_17 import my_enumerate
import unittest


class TestMyEnumerate(unittest.TestCase):
    def test_my_enumerate(self):
        self.assertEqual(list(my_enumerate([1, 2, 3])), [(0, 1), (1, 2), (2, 3)])
        self.assertEqual(list(my_enumerate("abc")), [(0, "a"), (1, "b"), (2, "c")])
        self.assertEqual(
            list(my_enumerate([1, 2, 3], start=1)), [(1, 1), (2, 2), (3, 3)]
        )
