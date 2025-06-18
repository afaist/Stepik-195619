"""
Рекурсивный обход дерева каталогов
"""

import os
import sys


def scan_dir(path, level=1):
    print("=" * 80)
    print("Level=", level, "Содержание:", os.listdir(path))
    for i in os.listdir(path):
        next = os.path.join(path, i)
        if os.path.isdir(next):
            print("Спускаемся", next)
            scan_dir(next, level + 1)
            print("Возвращаемся в", path)


if __name__ == "__main__":
    if len(sys.argv) == 2:
        scan_dir(sys.argv[1])
    else:
        print("Вы должны указать путь к каталогу")
