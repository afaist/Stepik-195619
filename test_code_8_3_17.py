from code_8_3_17 import grep
import unittest
import io
from unittest.mock import patch


class TestGrep(unittest.TestCase):
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_grep(self, mock_stdout):
        search = grep("кору")
        self.assertEqual(next(search), None)
        self.assertEqual(mock_stdout.getvalue(), "")
        search.send("Короед любит есть дерево")
        self.assertEqual(mock_stdout.getvalue(), "")
        search.send("Корутины полезно знать")
        self.assertEqual(mock_stdout.getvalue(), "Корутины полезно знать\n")
        search.send("Ненавижу бесконченые циклы")
        self.assertEqual(mock_stdout.getvalue(), "Корутины полезно знать\n")
        search.send("Ору с это задачи")
        self.assertEqual(mock_stdout.getvalue(), "Корутины полезно знать\n")
        search.send("Какая же эта тема про корутины непонятная")
        self.assertEqual(
            mock_stdout.getvalue(),
            "Корутины полезно знать\nКакая же эта тема про корутины непонятная\n",
        )
        search.close()
