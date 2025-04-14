"""
    Декоратор multiply_result_by

Создайте декоратор multiply_result_by, который принимает аргумент N и
возвращает функцию-декоратор, которая умножает результат декорированной функции
на N
"""

from functools import wraps
from collections.abc import Callable
from typing import Any


def multiply_result_by(
    n: int | float,
) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(func)
        def wrapper(*args: int | float, **kwargs: int | float) -> int | float:
            result = func(*args, **kwargs)
            return result * n

        return wrapper

    return decorator
