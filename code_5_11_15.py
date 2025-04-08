"""
    Декоратор check_count_args

Напишите декоратор check_count_args, который проверяет количество переданных
аргументов. Проверка заключается в следующем

    в оригинальную функцию должно быть передано только два аргумента и неважно
    позиционно или по ключу. Если это условие выполняется, возвращаем результат
    вызова оригинальной функции

    Если передано меньшее количество, декоратор должен вывести строку «Not
    enough arguments» и не должен запускать оригинальную функцию;

    Если передано более двух аргументов, то декоратор должен вывести строку
    «Too many arguments» и не должен запускать оригинальную функцию.

Не забывайте сохранять имя функции и строку документации. Для решения
необходимо написать только реализацию декоратора check_count_args
"""

from collections.abc import Callable
from typing import Any


def check_count_args(func: Callable[..., Any]) -> Callable[..., Any]:
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        if len(args) + len(kwargs) > 2:
            print("Too many arguments")
        elif len(args) + len(kwargs) < 2:
            print("Not enough arguments")
        else:
            return func(*args, **kwargs)

    wrapper.__doc__ = func.__doc__
    wrapper.__name__ = func.__name__
    return wrapper
