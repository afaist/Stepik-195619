"""
    Сумма списка

Напишите функцию sum_recursive, которая принимает на вход одномерный список из
целых чисел и возвращает сумму элементов переданного списка. Не забывайте, что
реализовать это нужно при помощи рекурсии.

Ваша задача только написать определение функции sum_recursive
"""


def sum_recursive(numbers: list[int]) -> int:
    if not numbers:
        return 0
    return numbers[0] + sum_recursive(numbers[1:])
