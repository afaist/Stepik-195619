"""
    Декоратор counting_calls

Реализуйте декоратор counting_calls, который будет подсчитывать количество
вызовов оригинальной функции.

После декорирования при помощи counting_calls у функции должен появиться
атрибут call_count, который отслеживает текущее количество вызовов.
"""

from functools import wraps


def counting_calls(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.call_count += 1
        return func(*args, **kwargs)

    setattr(wrapper, "call_count", 0)

    return wrapper
