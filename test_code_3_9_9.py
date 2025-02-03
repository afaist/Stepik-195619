from code_3_9_9 import make_order, tables
import unittest


class TestCode(unittest.TestCase):
    def test_make_order(self):
        make_order(1, soup="Borch")
        self.assertEqual(tables[1]["name"], "Andrey")
        self.assertEqual(tables[1]["is_vip"], True)
        self.assertEqual(tables[1]["order"]["soup"], "Borch")
