"""
    Декоратор add_attrs

Ваша задача написать параметризированный декоратор add_attrs, который принимает
произвольное количество именованных аргументов и на их основании добавляет
новые атрибуты для оригинальной функции
"""


def add_attrs(**attributes):
    def decorator(func):
        for key, value in attributes.items():
            setattr(func, key, value)
        return func

    return decorator
