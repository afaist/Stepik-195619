"""
     Декоратор counting_calls - 2

Усовершенствуем ранее созданный декоратор counting_calls, добавив отслеживание
переданных аргументов при каждом вызове.

Для этого декоратор counting_calls должен добавить в декорируемой функции
атрибут calls - список, в который будут сохраняться все переданные аргументы в
момент вызова в виде словаря. Каждый словарь должен иметь два ключа: args и
kwargs для сохранения соответствующих аргументов.
"""

from collections.abc import Callable
from typing import Any


def counting_calls(func: Callable) -> Callable:
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        calls = getattr(wrapper, "calls")
        calls.append({"args": args, "kwargs": kwargs})
        call_count = getattr(wrapper, "call_count")
        wrapper.__setattr__("call_count", call_count + 1)
        return func(*args, **kwargs)

    wrapper.__setattr__("calls", [])
    wrapper.__setattr__("call_count", 0)
    wrapper.__name__ = func.__name__
    wrapper.__doc__ = func.__doc__
    return wrapper


@counting_calls
def add(a: int, b: int) -> int:
    """Возвращает сумму двух чисел"""
    return a + b


print(add.__name__)
print(add.__doc__)

print(add(10, b=20))
print("Количество вызовов =", add.call_count)
print(add.calls)

print(add(5, 6))
print(add.calls[1])
