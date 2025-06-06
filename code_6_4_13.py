"""
Напишите функцию filter_numbers, которая принимает список целых чисел и
возвращает новый список, который состоит только из четных чисел входного
списка или из тех, которые по модулю больше 100.
"""


def filter_numbers(lst: list[int]) -> list[int]:
    return list(filter(lambda i: i % 2 == 0 or abs(i) > 100, lst))
