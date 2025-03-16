"""
Функция aggregation - 3

Перепишите функцию aggregation с прошлого шага так, чтобы у нее появился
необязательный параметр initial по умолчанию равный None. Данный параметр
отвечает за начальное состояние агрегации, если в него передать значение. Если
ничего не передавать в initial, то функция aggregation работает как прежде

"""


def aggregation(func, sequence: list | tuple, initial=None) -> int:
    start = 0
    if initial is not None:
        result = initial
    else:
        start = 1
        result = sequence[0]
    for x in sequence[start:]:
        result = func(result, x)
    return result


def get_add(x, y):
    return x + y


print(aggregation(get_add, [5, 2, 4, 3, 5], initial=10))
