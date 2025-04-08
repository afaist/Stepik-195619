"""
    Декоратор cache_result

Кэширование – это способ оптимизации работы приложения, при котором повторно
запрашиваемые данные сохраняются и далее используются для обслуживания
последующих запросов. Кешом называется место, куда будут сохраняться данные
после первого вызова.

Ваша задача написать декоратор cache_result, который оптимизирует
производительность за счет сохранения и извлечения результатов функций,
устраняя избыточные вычисления для повторяющихся входных данных и улучшая
скорость отклика приложения, особенно для длительных вычислений.

Взгляните на пример ниже

@cache_result
def multiply(a, b):
    return f"Product = {a * b}"

print(multiply(4, 5))  # Вызываем 1й раз функцию с аргументами 4 и 5. Идет сохранение результата

print(multiply(4, 5))  # При повторном вызове достаем из кеша

print(multiply(5, 8))  # Впервые вызывает с аргументами 5 и 8
print(multiply(5, 8))  # Достаем из кеша результат вызова multiply(5, 8)
print(multiply(5, 8))  # Вновь достаем из кеша

print(multiply(-3, 7))  # Впервые вычисляем результат вызова multiply(-3, 7), сохраняем в кеше
print(multiply(-3, 7))  # Достаем из кеша multiply(-3, 7)

Декоратор cache_result должен сохранять результат вызова оригинальной функции с
учетом передаваемых аргументов.

При повторном вызове функции с теми же аргументами, результат должен
возвращаться из кеша, предварительно сопроводив выводом следующего текста на
экран

[FROM CACHE] Вызов {имя_функции} = {результат_из_кеша}

Ваша задача написать только функцию-декоратор cache_result
"""

from collections.abc import Callable
from typing import Any


def cache_result(func: Callable) -> Callable:
    cache = {}

    def inner(*args: Any, **kwargs: Any) -> Any:
        key = str(args) + str(kwargs)
        result: Any = None
        if key in cache:
            result = cache[key]
            print(f"[FROM CACHE] Вызов {func.__name__} = {result}")
        else:
            result = func(*args, **kwargs)
            cache[key] = result
            # print(f"[FROM FUNCTION] Вызов {func.__name__} = {result}")
        return result

    inner.__name__ = func.__name__
    inner.__doc__ = func.__doc__
    return inner
