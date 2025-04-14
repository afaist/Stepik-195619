from code_5_12_10 import pass_arguments
import unittest


class TestPassArguments(unittest.TestCase):
    def test_add(self):
        @pass_arguments(1, 2, 3)
        def add(*values):
            return sum(values)

        self.assertEqual(add(5, 4, 6), 21)
        self.assertEqual(add(), 6)

    def test_concatenate(self):
        @pass_arguments(s="Когда", t="мы", u="встречаемся")
        def concatenate(**kwargs):
            return "".join(kwargs.values())

        self.assertEqual(
            concatenate(a="Я", b="не", c="знаю"), "ЯнезнаюКогдамывстречаемся"
        )
        self.assertEqual(concatenate(), "Когдамывстречаемся")
