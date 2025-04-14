"""
    Декоратор limit_query с параметром

Ваша задача переписать декоратор limit_query так, чтобы он ограничивал
разрешенное количество вызовов оригинальной функции по переданному параметру
limit. Когда декорируемая функция исчерпает лимит вызовов, необходимо выводить
на экран фразу

 «Лимит вызовов закончен, все <limit> попытки израсходованы»

Если лимит исчерпан, оригинальная функция не должна быть вызвана, декоратор
возвращает None
"""

from functools import wraps
from collections.abc import Callable
from typing import Any


def limit_query(limit: int) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        calls = 0

        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            nonlocal calls
            nonlocal limit

            if limit - calls <= 0:
                print(f"Лимит вызовов закончен, все {limit} попытки израсходованы")
                return None
            else:
                calls += 1
                return func(*args, **kwargs)

        return wrapper

    return decorator
