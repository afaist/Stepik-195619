"""
    Сумма списка

Напишите функцию sum_recursive, которая принимает на вход вложенный список,
конечными элементами которого являются целые числа, и возвращает сумму
элементов переданного списка. Уровень вложенности списка произвольный.

Ваша задача только написать определение рекурсивной функции sum_recursive
"""


def sum_recursive(lst: list[int | list]) -> int:
    total = 0
    for n in lst:
        if isinstance(n, list):
            sum_nested = sum_recursive(n)
            total += sum_nested
        else:
            total += n
    return total
