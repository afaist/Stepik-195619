"""
    Функция range - 2

Измените функцию-генератор my_range_gen так, чтобы она могла вызываться от
одного или двух аргументов.

Если вызов происходит от одного аргумента n, то my_range_gen  генерирует все
числа от 0 до n не включительно.

Если вызов происходит от двух аргументов a и b, то my_range_gen  генерирует все
числа от a включительно до b не включительно.
"""

from collections.abc import Iterator


def my_range_gen(a: int, b: int | None = None) -> Iterator[int]:
    if b is None:
        b = a
        a = 0
    for i in range(a, b):
        yield i
