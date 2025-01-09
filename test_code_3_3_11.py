from code_3_3_11 import is_pangram
import unittest


class PangramTest(unittest.TestCase):
    def test_pangram(self):
        self.assertTrue(is_pangram("the quick brown fox jumps over the lazy dog"))
        self.assertFalse(is_pangram("the quick brown fox jumps over the dog"))
        self.assertTrue(is_pangram("a quick brown fox jumps over the lazy dog"))
        self.assertTrue(is_pangram("How quickly daft jumping zebras vex!"))
        self.assertTrue(is_pangram("Pack my box with five dozen liquor jugs."))
