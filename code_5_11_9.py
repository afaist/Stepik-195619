"""
    Декоратор no_side_effects_decorator

Напишите декоратор no_side_effects_decorator, который защищает от побочных
действий функций
"""

from functools import wraps
from copy import deepcopy


def no_side_effects_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        new_args = [
            deepcopy(arg) if isinstance(arg, (list, set, dict)) else arg for arg in args
        ]
        new_kwargs = {
            k: deepcopy(v) if isinstance(v, (list, set, dict)) else v
            for k, v in kwargs.items()
        }
        return func(*new_args, **new_kwargs)

    return wrapper
