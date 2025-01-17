from code_3_7_14 import create_actor
import unittest


class TestCreateActor(unittest.TestCase):
    def test_create_actor(self):
        self.assertEqual(
            create_actor(), {"name": "Райан", "surname": "Рейнольдс", "age": 47}
        )
