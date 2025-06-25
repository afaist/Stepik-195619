"""
    Число-палиндром

Ваша задача — создать сопрограмму is_palindrome, которая проверяет поступающее
ей натуральное число на палиндром.

Числа поступают в сопрограмму при помощи метода send. Сопрограмма должна
порождать значение True, если число одинаково можно записать слева направо и
справа налево, в противном случае - значение False.

Вам необходимо написать только определение функции-сопрограммы is_palindrome.
"""

from collections.abc import Generator


def is_palindrome() -> Generator[bool, int, None]:
    """Checks whether a number is a polydrome

    Yields:
        return bool, get int
    """
    number: int | None = None
    while True:
        number = yield str(number) == str(number)[::-1]
