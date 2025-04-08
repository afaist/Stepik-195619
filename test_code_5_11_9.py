from code_5_11_9 import no_side_effects_decorator
import unittest


class TestNoSideEffectsDecorator(unittest.TestCase):
    def test_no_side_effects_decorator(self):
        @no_side_effects_decorator
        def add_element(data, element):
            data.append(element)
            return data

        my_list = [1, 2, 3]

        self.assertEqual(
            add_element(my_list, 4), [1, 2, 3, 4], "add_element() works incorrectly()"
        )
        self.assertEqual(
            add_element(my_list, 5), [1, 2, 3, 5], "add_element() works incorrectly()"
        )
        self.assertListEqual(my_list, [1, 2, 3])
