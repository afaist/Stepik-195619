from code_3_2_8 import overlapping
import unittest


class TestOverlapping(unittest.TestCase):
    def test_overlapping(self):
        assert overlapping(["this", "might", "work"], ["or", "maybe", "this"])
        assert not overlapping(["this", "might", "work"], ["or", "maybe", "that"])
        assert not overlapping(["I", "tink", "I am", 19], ["19", "bananas"])
