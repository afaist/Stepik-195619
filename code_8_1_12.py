"""
    Генератор квадратов

Ваша задача создать функцию-генератор gen_squares, которая принимает аргумент n
и генерирует квадраты чисел от 1 до n включительно. Ниже несколько вариантов
использования:

Ваша задача написать только определение функции gen_squares
"""

from typing import Iterator


def gen_squares(n: int) -> Iterator[int]:
    number = 1
    while number <= n:
        yield number * number
        number += 1
