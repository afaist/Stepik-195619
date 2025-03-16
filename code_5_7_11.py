"""
    Функция aggregation - 2

Перепишите функцию aggregation так, чтобы она возвращала итоговое значение
агрегации.

Функция aggregation по-прежнему должна принимать на вход функцию func и
коллекцию элементов sequence.
"""


def aggregation(func, sequence: list | tuple) -> list:
    result = sequence[0]
    for x in sequence[1:]:
        result = func(result, x)
    return result
