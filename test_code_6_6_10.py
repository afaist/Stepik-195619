from code_6_6_10 import get_words_with_position
import unittest


class TestCode(unittest.TestCase):
    def test_get_words_with_position(self):
        self.assertEqual(
            get_words_with_position("variation random electronics competence collapse"),
            [
                ("variation", 1),
                ("random", 2),
                ("electronics", 3),
                ("competence", 4),
                ("collapse", 5),
            ],
        )
