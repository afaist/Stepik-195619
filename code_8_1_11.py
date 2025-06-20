"""
    Функция range - 1

Ваша задача создать функцию-генератор my_range_gen, которая имеет один параметр n.

Функция my_range_gen должна генерировать по порядку все числа от 0 до n не
включительно. В общем, быть копией встроенной функции range, вызванной от
одного аргумента.

Ваша задача написать только определение функции-генератора my_range_gen
"""

from typing import Iterator


def my_range_gen(n: int) -> Iterator[int]:
    number = 0
    while number < n:
        yield number
        number += 1
