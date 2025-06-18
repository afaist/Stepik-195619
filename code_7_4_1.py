"""
Суммирование списков чисел различной вложенности
"""


def get_sum(numbers):
    total = 0
    for number in numbers:
        if isinstance(number, list):
            total += get_sum(number)
        else:
            total += number
    return total
