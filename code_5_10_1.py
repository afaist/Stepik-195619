"""
    Декоратор-повторитель

Напишите декоратор repeater, который трижды вызывает декорированную функцию

Ваша задача написать только определение функции декоратора repeater
"""


def repeater(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
        func(*args, **kwargs)

    return wrapper


@repeater
def multiply(num1, num2):
    print(num1 * num2)


multiply(9, 4)
