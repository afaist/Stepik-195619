"""
Test for functions from code_6_4_16.py
"""

from code_6_4_16 import filter_tuples
import unittest


class TestFilterTuples(unittest.TestCase):
    def test_filter_tuples(self):
        self.assertEqual(
            filter_tuples(
                (
                    (1, 2, 3),
                    (1, 2, 30),
                    (1, 20, 3),
                    (15, 2, 3),
                    (10, 2, 3),
                    (10, 20, 30),
                )
            ),
            ((1, 2, 30), (1, 20, 3), (10, 2, 3)),
        )
        self.assertEqual(
            filter_tuples(
                (
                    (1, 2, 3),
                    (1, 2, 30),
                    (1, 20, 3),
                    (5, 3, 4),
                    (5, 12, 1),
                    (5, 12, 0),
                    (5, 5, 12),
                    (15, 2, 3),
                    (10, 2, 3),
                    (10, 20, 30),
                    (1, 2, 30),
                    (60, 1, 1),
                    (60, 1, 0),
                    (20, 2, 2),
                )
            ),
            (
                (1, 2, 30),
                (1, 20, 3),
                (5, 3, 4),
                (5, 12, 1),
                (10, 2, 3),
                (1, 2, 30),
                (60, 1, 1),
            ),
        )
