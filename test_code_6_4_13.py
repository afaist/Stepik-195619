"""
Test for code_6_4_13.py
"""

from code_6_4_13 import filter_numbers
import unittest


class TestFilterNumbers(unittest.TestCase):
    def test_filter_numbers(self):
        self.assertEqual(filter_numbers([1, 2, 3, 4, 5]), [2, 4])
        self.assertEqual(filter_numbers([1, 2, 3, 4, 5, 6]), [2, 4, 6])
        self.assertEqual(
            filter_numbers([100, -200, 300, -400, 500]), [100, -200, 300, -400, 500]
        )
