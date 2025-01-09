from code_3_3_14 import reserve_table, delete_reservation
from tables import tables
import unittest


class TestCode3_3_14(unittest.TestCase):
    def test_reserve_table(self):
        reserve_table(3, "Gena")
        self.assertEqual(tables[3], "Gena")
        reserve_table(4, "Artem")
        self.assertEqual(tables[4], "Artem")
        reserve_table(5, "Artur")
        self.assertNotEqual(tables[5], "Artur")
        self.assertEqual(tables[5], "Vasiliy")

    def test_delete_reservation(self):
        delete_reservation(3)
        self.assertEqual(tables[3], None)
        delete_reservation(1)
        self.assertEqual(tables[1], None)
