from code_3_7_13 import concatenate
import unittest


class TestConcatenate(unittest.TestCase):
    def test_concatenate(self):
        self.assertEqual(
            concatenate(a="Я", b="Выучу", c="Этот", d="Питон", e="!"),
            "ЯВыучуЭтотПитон!",
        )
        self.assertEqual(
            concatenate(first="i got ", second=5, third=" stars"), "i got 5 stars"
        )
        self.assertEqual(
            concatenate(q="iHave", w="next", e="Coins", r=[10, 5, 10, 7]),
            "iHavenextCoins[10, 5, 10, 7]",
        )
