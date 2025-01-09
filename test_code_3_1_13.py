from code_3_1_13 import is_dunder
import unittest


class Test_is_dunder(unittest.TestCase):
    def test_is_dunder(self):
        assert is_dunder("__init__")
        assert is_dunder("__getitem__")
        assert not is_dunder("get")
        assert not is_dunder("get_item")
        assert is_dunder("__str__")
        assert not is_dunder("___bool___")
        assert not is_dunder("__s__")
        assert not is_dunder("__abvc3__")
        assert not is_dunder("____")
        assert not is_dunder("_str__")
        assert not is_dunder("__str_")
        assert is_dunder("__ab__")
