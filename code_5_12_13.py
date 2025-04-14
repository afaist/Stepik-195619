"""
    Декоратор compose

Ваша задача написать параметризированный декоратор compose, который принимает
произвольное количество функций и применяет их последовательно к результату
декорируемой функции
"""

from typing import Any, Callable
from functools import wraps


def compose(*functions: Callable) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            result = func(*args, **kwargs)
            for f in functions:
                result = f(result)
            return result

        return wrapper

    return decorator
