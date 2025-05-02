"""
Test for code_6_3_12.py
Author: Firstname Lastname
Date: 2025-05-01
Description: Test for code_6_3_12.py
"""

from code_6_3_14 import convert_to_rgb
import unittest


class TestConvertToRGB(unittest.TestCase):
    def test_convert_to_rgb(self):
        self.assertEqual(
            convert_to_rgb(["#000000", "#FFFFFF", "#FF0000"]),
            [(0, 0, 0), (255, 255, 255), (255, 0, 0)],
        )
        self.assertEqual(
            convert_to_rgb(["#87CEEB", "#87CEFA", "#191970"]),
            [(135, 206, 235), (135, 206, 250), (25, 25, 112)],
        )
        self.assertEqual(
            convert_to_rgb(["#87CEEB", "#87CEFA", "#191970"]),
            [(135, 206, 235), (135, 206, 250), (25, 25, 112)],
        )
