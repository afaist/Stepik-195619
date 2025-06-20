"""
    Генератор бесконечной арифметической прогрессии

Ваша задача создать функцию-генератор gen_arithmetic_progression, которая при
вызове принимает два значения:

    первый элемент прогрессии
    разность элементов прогрессии

Функция-генератор gen_arithmetic_progression должна выдавать элементы
бесконечной арифметической прогрессии с учетом переданных значений

Ваша задача написать только определение функции-генератора
gen_arithmetic_progression
"""

from typing import Iterator


def gen_arithmetic_progression(first: int, difference: int) -> Iterator[int]:
    while True:
        yield first
        first += difference
