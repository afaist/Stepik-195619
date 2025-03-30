"""
    Фильтрация аргументов

Ваша задача создать два декоратора

    1️⃣ filter_even, который фильтрует только позиционные аргументы. Среди всех
      переданных значений он оставляет только четные числа, False и коллекции,
      длина которых четная

    2️⃣ delete_short, который фильтрует только именованные аргументы. Среди всех
      переданных значений он оставляет только те, имена которых более четырех
      символов
"""


def filter_even(func):
    def wrapper(*args, **kwargs):
        new_args = [
            arg
            for arg in args
            if (hasattr(arg, "__len__") and len(arg) % 2 == 0)
            or (isinstance(arg, int) and arg % 2 == 0)
            or arg is False
        ]
        return func(*new_args, **kwargs)

    return wrapper


def delete_short(func):
    def wrapper(*args, **kwargs):
        new_kwargs = {k: v for k, v in kwargs.items() if len(k) > 4}
        return func(*args, **new_kwargs)

    return wrapper
