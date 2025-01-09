from code_3_3_15 import reserve_table, delete_reservation, is_table_free, tables
import unittest


class TestCode_3_3_15(unittest.TestCase):
    def test_reserve_table(self):
        reserve_table(3, "Gena", True)
        self.assertEqual(tables[3], {"name": "Gena", "is_vip": True})
        reserve_table(4, "Artem", False)
        self.assertEqual(tables[4], {"name": "Artem", "is_vip": False})
        reserve_table(5, "Vlad", True)
        self.assertEqual(tables[5], {"name": "Vasiliy", "is_vip": False})

    def test_delete_reservation(self):
        delete_reservation(5)
        self.assertEqual(tables[5], None)
        reserve_table(5, "Vasiliy", False)
