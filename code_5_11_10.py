"""
    Декоратор add_args

Напишите декоратор add_args, который добавляет к переданным аргументам еще два
значения: строку «begin» в начало аргументов, строку «end» в конец. Также
декоратор должен сохранить первоначальное имя декорируемой функции и ее строку
документации
"""


def add_args(func):
    def wrapper(*args):
        new_args = ["begin"] + list(args) + ["end"]
        return func(*new_args)

    wrapper.__name__ = func.__name__
    wrapper.__doc__ = func.__doc__
    return wrapper
