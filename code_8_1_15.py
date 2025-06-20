"""
    Генератор факториалов

Напишите генератор-функцию gen_factorial, которая принимает натуральное число n
и генерирует факториалы чисел от 1! до n!
"""

from collections.abc import Iterator


def gen_factorial(n: int) -> Iterator[int]:
    x = 1
    for i in range(1, n + 1):
        x *= i
        yield x
