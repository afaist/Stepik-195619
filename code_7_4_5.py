"""
    Превращаем вложенный список в плоский

Представьте, что у нас есть список целых чисел неограниченной вложенности. То
есть наш список может состоять из списков, внутри которых также могут быть
списки. Задача функции flatten вернуть новый линейный список, составленный из
элементов входного списка, в котором уже отсутствует какая-либо вложенность.
Элементы в плоском списке должны располагаться в том же порядке, как они
следовали в исходном списке.

Ваша задача — написать только определение функции flatten.

Разбор Youtube Patreon Boosty
"""

NestedList = list["int | NestedList"]


def flatten(numbers: NestedList) -> list[int]:
    result = []
    for elements in numbers:
        if isinstance(elements, list):
            result.extend(flatten(elements))
        else:
            result.append(elements)
    return result
