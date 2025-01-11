"""
Напишите функцию product , которая принимает список чисел и находит их
произведение. Также данная функция может принимать необязательный параметр
start , который отвечает за начальное значение произведения (по умолчанию равно
1)
"""


def product(numbers: list, start: int = 1) -> int:
    result = start
    for number in numbers:
        result *= number
    return result
