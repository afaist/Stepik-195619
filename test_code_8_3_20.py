from code_8_3_20 import get_average
import unittest


class TestGetAverage(unittest.TestCase):
    def test_get_average(self):
        coro = get_average()
        self.assertEqual(next(coro), None)
        self.assertEqual(coro.send(10), 10)
        self.assertEqual(coro.send(20), 15)
        self.assertEqual(coro.send(6), 12)
        coro.close()

    def test_get_average_2(self):
        coro = get_average()
        self.assertEqual(next(coro), None)
        self.assertEqual(coro.send(10), 10)
        self.assertEqual(coro.send(20), 15)
        self.assertEqual(coro.send(30), 20)
        self.assertEqual(coro.send(40), 25)
        self.assertEqual(coro.send(50), 30)
        coro.close()
