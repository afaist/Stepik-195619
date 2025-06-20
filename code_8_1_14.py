"""
    Генератор последовательности Фибоначчи

Ваша задача создать функцию-генератор gen_fibonacci_numbers, которая принимает
аргумент n и генерирует n-ое количество чисел Фибоначчи.

Будем считать, что последовательность Фибоначчи такая: 1, 1, 2, 3, 5, 8, 13,
21, 34, ...

Ваша задача написать только определение функции gen_fibonacci_numbers
"""

from typing import Iterator


def gen_fibonacci_numbers(n: int) -> Iterator[int]:
    a, b = 1, 1
    for _ in range(n):
        yield a
        a, b = b, a + b
