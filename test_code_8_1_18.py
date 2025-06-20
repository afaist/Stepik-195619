from code_8_1_18 import chunker
import unittest


class TestChunker(unittest.TestCase):
    def test_chunker(self):
        self.assertEqual(
            list(chunker(range(10), 3)),
            [range(0, 3), range(3, 6), range(6, 9), range(9, 10)],
        )
