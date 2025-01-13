"""
    Чистый lstrip

Напишите функцию lstrip, которая принимает список lst и значение value. Функция
lstrip должна теперь создать новый список, который является копией lst, но без
элементов в самом начале, равных значению value. Изначальный список, переданный
в lst, не должен измениться
"""


def lstrip(lst, value):
    new_lst = lst.copy()
    while new_lst and new_lst[0] == value:
        new_lst.pop(0)
    return new_lst
