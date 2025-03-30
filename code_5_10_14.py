"""
    Валидация kwargs

Напишите декоратор validate_all_kwargs_int_pos, который проверяет на корректность переданные именованные аргументы. Корректным будет считаться именованный аргумент, значение которого является целым положительным числом. Позиционные аргументы игнорируются во время проверки декоратора validate_all_kwargs_int_pos.

Если было передано хотя бы одно некорректное значение в именованный аргумент, функция-декоратор validate_all_kwargs_int_pos должна:

    вывести на экран фразу «Все именованные аргументы должны быть положительными числами»;

    вернуть None и не запускать оригинальную  функцию.

Если же все аргументы корректны, validate_all_kwargs_int_pos запускает оригинальную функцию со всеми переданными значениями.

Также для проверки вам необходимо скопировать из предыдущего шага реализацию декоратора validate_all_args_str, потому что в проверках будет использоваться валидация сразу и на *args, и на **kwargs.

"""


def validate_all_kwargs_int_pos(func):
    def wrapper(*args, **kwargs):
        for _, value in kwargs.items():
            if not isinstance(value, int) or value <= 0:
                print("Все именованные аргументы должны быть положительными числами")
                return None
        return func(*args, **kwargs)

    return wrapper


def validate_all_args_str(func):
    def inner(*args, **kwargs):
        if any(map(lambda x: not isinstance(x, str), args)):
            print("Все аргументы должны быть строками")
            return
        return func(*args, **kwargs)

    return inner
