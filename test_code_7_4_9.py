from code_7_4_9 import flatten_dict
import unittest


class TestFlattenDict(unittest.TestCase):
    def test_flatten_dict(self):
        input_dict = {"a": 1, "b": {"c": 2, "d": 3}}
        expected_output = {"a": 1, "b_c": 2, "b_d": 3}
        self.assertEqual(flatten_dict(input_dict), expected_output)
        self.assertEqual(flatten_dict({}), {})
        self.assertEqual(
            flatten_dict({"Q": {"w": {"E": {"r": {"T": {"y": 123}}}}}}),
            {"Q_w_E_r_T_y": 123},
        )
        self.assertEqual(
            flatten_dict(
                {
                    "Germany_berlin": 7,
                    "Europe_italy_Rome": 3,
                    "USA_washington": 1,
                    "USA_New York": 4,
                }
            ),
            {
                "Germany_berlin": 7,
                "Europe_italy_Rome": 3,
                "USA_washington": 1,
                "USA_New York": 4,
            },
        )
