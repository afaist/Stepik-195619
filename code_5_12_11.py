"""
    Декоратор convert_to

Напишите декоратор convert_to, который позволяет автоматически преобразовать
возвращаемое значение в указанный тип данных. Функция-декоратор convert_to
имеет обязательный параметр type_, в который необходимо передать тип данных для
дальнейшего преобразования.
"""

from functools import wraps


def convert_to(type_):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return type_(result)

        return wrapper

    return decorator
