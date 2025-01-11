from code_3_4_11 import add_item, shopping_list
import unittest


class TestCode(unittest.TestCase):
    def test_add_item(self):
        add_item("Bread", 10)
        self.assertEqual(shopping_list, {"Bread": 10})
        add_item("Milk")
        self.assertEqual(shopping_list, {"Bread": 10, "Milk": 1})
        add_item("Orange", 3)
        self.assertEqual(shopping_list, {"Bread": 10, "Milk": 1, "Orange": 3})
        add_item("Bread", 3)
        self.assertEqual(shopping_list, {"Bread": 13, "Milk": 1, "Orange": 3})
