"""
Напишите функцию-генератор my_enumerate, которая копирует работу встроенной
функции enumerate.
"""

from typing import Iterable, Iterator


def my_enumerate(iterable: Iterable, start: int = 0) -> Iterator:
    count = start
    for item in iterable:
        yield count, item
        count += 1
