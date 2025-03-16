"""
    Множественное вычисление-2

Затем создайте функцию compute, которая принимает список функций и произвольное
количество значений. Функция compute должна применить последовательно в
переданном порядке все функции сразу к каждому значению и сформировать из
полученных значений новый список, который и будет возвращаться в качестве
ответа
"""


def compute(functions: list, *args) -> list:
    "Use every function in functions on every value in args"
    result = []
    for val in args:
        for f in functions:
            val = f(val)
        result.append(val)

    return result


def square(num):
    "Return the square of num"
    return num**2


def inc(num):
    "Return num+1"
    return num + 1


def dec(num):
    "Return num - 1"
    return num - 1


print(compute([square, inc], 10))
