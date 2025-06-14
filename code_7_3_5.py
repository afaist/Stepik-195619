"""
    Наибольший общий делитель

Перед вами реализация функции gcd, которая находит наибольший общий делитель
при помощи итерации

def gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a

Перепишите данную программу при помощи рекурсии
"""


def gcd(a: int, b: int) -> int:
    """Наибольший общий делитель с помощью рекурсии

    Args:
        a: целое число
        b: целое число

    Returns:
        Наибольший общий делитель переданных чисел
    """
    if b == 0:
        return a
    return gcd(b, a % b)
