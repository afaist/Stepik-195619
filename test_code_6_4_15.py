"""Тест функции get_values из модуля code_6_4_15

Тесты предоставлены в заданиях
"""

from code_6_4_15 import get_values
import unittest


class TestGetValues(unittest.TestCase):
    def test_get_values(self):
        self.assertEqual(
            get_values((2, 12, 5, 9, 3, 16, 7, 13, 21, 1, 15, 4, 20, 11)),
            (36, 27, 9, 63, 45),
        )
        self.assertEqual(
            get_values((2, 0, 3, 4, 7, 13, 21, 1, 15, 9, 11)), (0, 9, 63, 45, 27)
        )
