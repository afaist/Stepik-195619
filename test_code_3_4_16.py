from code_3_4_16 import calculate_per_person
import unittest


class TestCalculatePerPerson(unittest.TestCase):
    def test_calculate_per_person(self):
        self.assertEqual(calculate_per_person(100, 2, 0), 50.0)
        self.assertEqual(calculate_per_person(100, 2, 20), 60.0)
        self.assertEqual(calculate_per_person(100, 3, 20), 40.0)
        self.assertEqual(calculate_per_person(100, 3, 10), 36.67)
        self.assertEqual(calculate_per_person(100, 5), 22.0)
