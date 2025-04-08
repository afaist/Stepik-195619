"""
    Декоратор monkey_patching

Monkey patch -  это прием в программировании, который используется для
динамического изменения поведения фрагмента кода во время выполнения.

Ваша задача написать декоратор monkey_patching, который заменяет значения всех
переданных аргументов при вызове оригинальной функции следующим образом:

    ➕   значение каждого позиционного аргумента заменяется на строку «Monkey»

    ➕   значение каждого именованного аргумента заменяется на строку «patching»
"""

from functools import wraps


def monkey_patching(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        new_args = ["Monkey" for _ in args]
        new_kwargs = {key: "patching" for key in kwargs}
        return func(*new_args, **new_kwargs)

    return wrapper
