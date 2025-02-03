"""
Как правильно вызвать функцию item_sum  и при этом передать распакованные
значения переменных my_list  и  my_dict ?
"""


def item_sum(*args, **kwargs):
    print(args, kwargs)
    current_sum = 0
    for arg in args:
        current_sum += arg

    for kwarg in kwargs.values():
        current_sum += kwarg
    return current_sum


my_list = [5, 19, 23, 88]
my_dict = {"a": 11, "b": 23}

print(item_sum(*my_list, **my_dict))
