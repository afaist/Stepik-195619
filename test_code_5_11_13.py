from code_5_11_13 import monkey_patching
import unittest


class TestMonkeyPatching(unittest.TestCase):
    def test_concatenate(self):
        @monkey_patching
        def concatenate(*args):
            """
            Возвращает конкатенацию переданных строк
            """
            return ", ".join(args)

        self.assertEqual(
            concatenate("Hello", "world", "my", "name is", "Artem"),
            "Monkey, Monkey, Monkey, Monkey, Monkey",
        )
        self.assertEqual(
            concatenate("my", "name is", "Artem"),
            "Monkey, Monkey, Monkey",
        )
        self.assertEqual(concatenate.__name__, "concatenate")
        self.assertEqual(
            concatenate.__doc__.strip(), "Возвращает конкатенацию переданных строк"
        )

    def test_info_kwargs(self):
        @monkey_patching
        def info_kwargs(**kwargs):
            """Выводит информацию о переданных kwargs"""
            return [key + " = " + val for key, val in kwargs.items()]

        self.assertEqual(
            info_kwargs(first_name="Artem", last_name="Petrov"),
            ["first_name = patching", "last_name = patching"],
        )
