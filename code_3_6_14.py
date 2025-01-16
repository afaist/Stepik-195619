"""
    Напишите функцию check_sum, которая принимает произвольное количество
    аргументов типа int.

Данная функция должна вывести на экран фразу «not enough», если сумма всех
элементов меньше 50, в противном случае нужно вывести «verification passed»

Вам необходимо написать только определение функции check_sum
"""


def check_sum(*args):
    if sum(args) >= 50:
        print("verification passed")
    else:
        print("not enough")
