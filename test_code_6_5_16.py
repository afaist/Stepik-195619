from code_6_5_16 import get_info_marks
import unittest


class TestGetInfoMarks(unittest.TestCase):
    def test_get_info_marks(self):
        math = [90, 76, 94]
        history = [78, 79, 90]
        students = ["Marie", "Michael", "Marge"]
        self.assertEqual(
            get_info_marks(students, math, history),
            {
                "Marie": {"best": 90, "worst": 78},
                "Michael": {"best": 79, "worst": 76},
                "Marge": {"best": 94, "worst": 90},
            },
        )

    def test_get_info_marks_empty(self):
        self.assertEqual(get_info_marks([], []), {})

    def test_get_info_marks_one_student(self):
        self.assertEqual(
            get_info_marks(["Marie"], [90]), {"Marie": {"best": 90, "worst": 90}}
        )

    def test_get_info_marks_2(self):
        math = [90, 76, 94]
        history = [78, 79, 90]
        geography = [95, 80, 92]
        students = ["Marie", "Michael", "Marge"]
        self.assertEqual(
            get_info_marks(students, math, geography, history),
            {
                "Marie": {"best": 95, "worst": 78},
                "Michael": {"best": 80, "worst": 76},
                "Marge": {"best": 94, "worst": 90},
            },
        )

    def test_get_info_marks_3(self):
        math = [90, 76, 94]
        history = [78, 79, 90]
        geography = [95, 80, 92]
        music = [93, 98, 100]
        students = ["Marie", "Michael", "Marge"]
        self.assertEqual(
            get_info_marks(students, math, geography, history, music),
            {
                "Marie": {"best": 95, "worst": 78},
                "Michael": {"best": 98, "worst": 76},
                "Marge": {"best": 100, "worst": 90},
            },
        )
