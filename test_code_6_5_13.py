from code_6_5_13 import create_info
import unittest

print("Testing create_info function...")


class TestCreateInfo(unittest.TestCase):
    def test_create_info_1(self):
        names = ["Pankratiy", "Lidochka", "Svetka", "Maks", "Yura", "Sergei"]

        ids = [77, 4, 20, 37, 32, 96]
        self.assertEqual(
            create_info(names, ids),
            {
                4: "Lidochka",
                20: "Maks",
                32: "Pankratiy",
                37: "Sergei",
                77: "Svetka",
                96: "Yura",
            },
        )

    def test_create_info_2(self):
        names = [
            "Pankratiy",
            "Lidochka",
            "Innokentiy",
            "Anfisa",
            "Yaroslava",
            "Svetka",
            "Maks",
            "Yura",
            "Sergei",
        ]

        ids = [77, 4, 20, 5, 56, 17, 20, 32, 96]
        self.assertEqual(
            create_info(names, ids),
            {
                4: "Anfisa",
                5: "Innokentiy",
                17: "Lidochka",
                20: "Pankratiy",
                32: "Sergei",
                56: "Svetka",
                77: "Yaroslava",
                96: "Yura",
            },
        )
