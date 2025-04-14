"""
    Декоратор monkey_patching - 2

Ваша задача переписать декоратор monkey_patching. Ранее он заменял значения
всех переданных аргументов при вызове оригинальной функции следующим образом:

    ➕   значение каждого позиционного аргумента заменяется на строку «Monkey»

    ➕   значение каждого именованного аргумента заменяется на строку
    «patching»

Теперь необходимо завести параметры arg и kwarg, при помощи которых можно
влиять на значения, которые будут проставляться в позиционные и именованные
аргументы. Параметры arg и kwarg являются необязательными для передачи, их
значения по умолчанию «Monkey» и «patching» соответственно.
"""

from typing import Any
from collections.abc import Callable
from functools import wraps


def monkey_patching(
    arg: str = "Monkey", kwarg: str = "patching"
) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(func)
        def wrapper(*args: tuple, **kwargs: dict) -> Any:
            new_args = [arg] * len(args)
            new_kwargs = {key: kwarg for key in kwargs}
            return func(*new_args, **new_kwargs)

        return wrapper

    return decorator
