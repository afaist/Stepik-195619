from code_5_10_4 import uppercase_elements
import unittest


@uppercase_elements
def list_fun():
    return ["monarch", "Touch", "officiaL", "DangerouS", "breathe"]


@uppercase_elements
def list_fun_01(name, surname):
    return ["temple", "store", name, surname, *[1, 2, 3]]


@uppercase_elements
def dict_fun():
    return {
        "monarch": 1,
        "Touch": 2,
        "officiaL": 3,
        "DangerouS": 4,
        "breathe": 5,
        4: "hello",
    }


class TestUpperCaseElements(unittest.TestCase):
    def test_list(self):
        self.assertEqual(
            list_fun(), ["MONARCH", "TOUCH", "OFFICIAL", "DANGEROUS", "BREATHE"]
        )
        self.assertEqual(
            list_fun_01("Gerard", "Pique"),
            ["TEMPLE", "STORE", "GERARD", "PIQUE", 1, 2, 3],
        )

    def test_dict(self):
        self.assertEqual(
            dict_fun(),
            {
                "MONARCH": 1,
                "TOUCH": 2,
                "OFFICIAL": 3,
                "DANGEROUS": 4,
                "BREATHE": 5,
                4: "hello",
            },
        )
