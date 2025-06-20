"""
    Генератор нечетных чисел

Напишите генератор-функцию gen_odd, которая принимает натуральное число n и
генерирует последовательность нечетных чисел от 1 до n включительно
"""

from collections.abc import Generator


def gen_odd(n: int) -> Generator[int]:
    for i in range(1, n + 1, 2):
        yield i
