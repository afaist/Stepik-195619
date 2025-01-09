from code_3_3_12 import translate_to_robber_lang
import unittest


class TranslateTests(unittest.TestCase):
    def test_translate(self):
        self.assertEqual(translate_to_robber_lang("hello"), "hohelollolo")
        self.assertEqual(
            translate_to_robber_lang("This is kinda fun"),
            "ToThohisos isos kokinondoda fofunon",
        )
        self.assertEqual(
            translate_to_robber_lang("I Think YoU Might BE righT!"),
            "I ToThohinonkok YoYoU MoMigoghohtot BoBE rorigoghohToT!",
        )
