"""
    Удваиваем результат

Напишите декоратор double_it, который возвращает удвоенный результат вызова
декорированной функции

Ваша задача написать только определение функции декоратора double_it
"""


def double_it(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs) * 2

    return wrapper


@double_it
def multiply(num1, num2):
    return num1 * num2


res = multiply(
    9, 4
)  # произведение 9*4=36, но декоратор double_it удваивает это значение
print(res)
