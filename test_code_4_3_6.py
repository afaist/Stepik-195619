from code_4_3_6 import get_first_repeated_word
import unittest
import typing


class TestCode(unittest.TestCase):
    def test_first_repeated_word(self):
        self.assertEqual(get_first_repeated_word(["hello", "world"]), None)
        self.assertEqual(get_first_repeated_word(["hello", "hello"]), "hello")
        self.assertEqual(get_first_repeated_word(["hello", "world", "hello"]), "hello")
        self.assertEqual(get_first_repeated_word.__name__, "get_first_repeated_word")
        self.assertEqual(
            get_first_repeated_word.__doc__, "Находит первый дубль в списке"
        )
        self.assertEqual(
            get_first_repeated_word.__annotations__,
            {"words": typing.List[str], "return": typing.Optional[str]},
        )
