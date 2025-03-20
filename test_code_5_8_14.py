from code_5_8_14 import create_dict
import unittest


class TestCreateDict(unittest.TestCase):
    def test_create_dict(self):
        f_3 = create_dict()
        self.assertEqual(f_3(["name", "test"]), {1: ["name", "test"]})

    def test_create_dict_f1(self):
        f_1 = create_dict()
        self.assertEqual(f_1("privet"), {1: "privet"})
        self.assertEqual(f_1("test"), {1: "privet", 2: "test"})
        self.assertEqual(f_1("poka"), {1: "privet", 2: "test", 3: "poka"})
