from code_6_3_10 import convert_to
import unittest


class TestConvertTo(unittest.TestCase):
    def test_convert_to_str(self):
        self.assertEqual(
            convert_to([116, -411, 448, 636, -254, -295, 220, 216, 187, -150], str),
            [
                "116",
                "-411",
                "448",
                "636",
                "-254",
                "-295",
                "220",
                "216",
                "187",
                "-150",
            ],
        )

    def test_convert_to_int(self):
        self.assertEqual(
            convert_to([116, -411, 448, 636, -254, -295, 220, 216, 187, -150], int),
            [116, -411, 448, 636, -254, -295, 220, 216, 187, -150],
        )
        self.assertEqual(
            convert_to(["-383", "-101", "121", "40", "278", "118", "-462"]),
            [-383, -101, 121, 40, 278, 118, -462],
        )
