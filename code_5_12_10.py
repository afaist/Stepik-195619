"""
    Декоратор pass_arguments

Ваша задача написать параметризированный декоратор pass_arguments, который
принимает произвольное количество именованных и позиционных аргументов и
пробрасывает их дополнительно к аргументам, которые передаются при вызове
оригинальной функции
"""

from functools import wraps
from typing import Any
from collections.abc import Callable


def pass_arguments(
    *args: Any, **kwargs: Any
) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(func)
        def wrapper(*args2: Any, **kwargs2: Any) -> Any:
            return func(*args2 + args, **kwargs2 | kwargs)

        return wrapper

    return decorator
