"""
    Нахождение самого большого элемента списка

Напишите функцию get_max_recursive, которая принимает на вход вложенный список,
конечными элементами которого являются целые числа, и возвращает самый большой
элемент переданного списка. Уровень вложенности исходного списка произвольный.

Ваша задача только написать определение рекурсивной функции get_max_recursive
"""

Nestedlist = list["Nestedlist | int"]


def get_max_recursive(numbers: Nestedlist) -> int:
    max_element = -999999999999999999999999999
    for element in numbers:
        if isinstance(element, list):
            max_element = max(max_element, get_max_recursive(element))
        else:
            max_element = max(max_element, element)
    return max_element
