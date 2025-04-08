"""
Test for decorator counting_calls
"""

from code_5_11_14 import counting_calls
import unittest


class TestCountingCalls(unittest.TestCase):
    def test_counting_calls(self):
        @counting_calls
        def f():
            pass

        f()
        f()
        f()
        self.assertEqual(f.call_count, 3)

    def test_add(self):
        @counting_calls
        def add(a, b):
            """
            Возвращает сумму двух чисел
            """
            return a + b

        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add.call_count, 1)
        self.assertEqual(
            add.__doc__.strip(),
            "Возвращает сумму двух чисел",
        )
