from code_6_5_14 import zip_with_function
import unittest


class TestZipWithFunction(unittest.TestCase):
    def test_zip_with_function(self):
        self.assertEqual(
            zip_with_function([[1, 2, 3], [4, 5, 6]], lambda x, y: x + y), [5, 7, 9]
        )

    def test_sum_zip_with_function(self):
        def get_sum_two_numbers(a: int, b: int) -> int:
            return a + b

        self.assertEqual(
            zip_with_function([[1, 2, 4], [3, 5, 8]], get_sum_two_numbers), [4, 7, 12]
        )

    def test_three_sum_zip_with_function(self):
        def get_sum_three_numbers(a: int, b: int, c: int) -> int:
            return a + b + c

        self.assertEqual(
            zip_with_function([[2, 5, 8], [3, 4, 7], [5, 6, 5]], get_sum_three_numbers),
            [10, 15, 20],
        )
