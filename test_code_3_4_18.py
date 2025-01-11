from code_3_4_18 import create_matrix
import unittest


class TestCreateMatrix(unittest.TestCase):
    def test_create_matrix(self):
        self.assertEqual(create_matrix(), [[1, 0, 0], [0, 2, 0], [0, 0, 3]])
        self.assertEqual(create_matrix(size=2), [[1, 0], [0, 2]])
        self.assertEqual(create_matrix(size=3), [[1, 0, 0], [0, 2, 0], [0, 0, 3]])
        self.assertEqual(create_matrix(up_fill=7), [[1, 7, 7], [0, 2, 7], [0, 0, 3]])
        self.assertEqual(
            create_matrix(up_fill=7, down_fill=8), [[1, 7, 7], [8, 2, 7], [8, 8, 3]]
        )
