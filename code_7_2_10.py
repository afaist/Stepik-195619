"""
    Наименьшее число в списке

Напишите рекурсивную функцию find_min, которая найдет наименьшее число в
списке. Для этого функция принимает в качестве аргумента список для поиска
наименьшего значения
"""


def find_min(list: list[int | float]) -> int | float:
    if len(list) == 1:
        return list[0]
    else:
        return min(list[0], find_min(list[1:]))
