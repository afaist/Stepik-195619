from code_5_5_15 import find_keys
import unittest


class TestFindKeys(unittest.TestCase):
    def test_find_keys(self):
        result = find_keys(
            marks=[4, 5], name="Ashle", surname="Brown", age=20, Also=(1, 2)
        )
        self.assertEqual(result, ["Also", "marks"])
        result = find_keys(At=[4], awaited=(3,), aDobe=[5])
        self.assertEqual(result, ["aDobe", "At", "awaited"])
