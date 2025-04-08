"""
    Декоратор reverse

Реализуйте декоратор reverse, который сделает так, чтобы декорированная функция
принимала все свои позиционные аргументы в обратном порядке. Именованные
аргументы должны игнорироваться декоратором reverse.

Также нужно сохранить информацию о декорируемой функции.
"""


def reverse(func):
    def wripper(*args, **kwargs):
        args = args[::-1]
        return func(*args)

    wripper.__name__ = func.__name__
    wripper.__doc__ = func.__doc__
    return wripper
