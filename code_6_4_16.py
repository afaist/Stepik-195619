"""
    Напишите функцию filter_tuples, которая принимает кортеж кортежей из трех числовых значений.

Функция filter_tuples должна вернуть новый кортеж, который состоит только из
тех элементов входного кортежа, произведение значений которых равно 60
"""


def filter_tuples(
    numbers: tuple[tuple[int, int, int], ...],
) -> tuple[tuple[int, int, int], ...]:
    return tuple(filter(lambda x: x[0] * x[1] * x[2] == 60, numbers))
