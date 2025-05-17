from code_6_5_15 import get_info_marks
import unittest


class TestGetInfoMarks(unittest.TestCase):
    def test_get_info_marks(self):
        math = [90, 76, 94]
        history = [78, 79, 90]
        students = ["Marie", "Michael", "Marge"]
        self.assertEqual(
            get_info_marks(students, math, history),
            {"Marie": 90, "Michael": 79, "Marge": 94},
        )

    def test_get_info_marks_empty(self):
        self.assertEqual(get_info_marks([], []), {})

    def test_get_info_marks_one_student(self):
        self.assertEqual(get_info_marks(["Marie"], [90]), {"Marie": 90})

    def test_get_info_marks_2(self):
        math = [90, 76, 94]
        history = [78, 79, 90]
        geography = [95, 80, 92]
        students = ["Marie", "Michael", "Marge"]
        self.assertEqual(
            get_info_marks(students, math, geography, history),
            {"Marie": 95, "Michael": 80, "Marge": 94},
        )

    def test_get_info_marks_3(self):
        math = [90, 76, 94]
        history = [78, 79, 90]
        geography = [95, 80, 92]
        music = [93, 98, 100]
        students = ["Marie", "Michael", "Marge"]
        self.assertEqual(
            get_info_marks(students, math, geography, history, music),
            {"Marie": 95, "Michael": 98, "Marge": 100},
        )
