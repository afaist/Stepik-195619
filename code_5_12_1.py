"""
    Пример применения параметризированного декоратора

Мы создадим декоратор-функцию cached_with_expiry, который позволит нам
кешировать данные, причем с возможностью хранения данных в кеше на определенное
время. Данные в кеше будут храниться заведомо известное количество времени, по
истечению которого мы будем считать, что данные становятся устаревшими и уже не
могут быть использованы.
"""

import time
from functools import wraps


def cached_with_expiry(expiry_time):
    def decorator(func):
        cache = {}

        @wraps(func)
        def wrapper(*args, **kwargs):
            nonlocal cache
            key = (*args, *kwargs.items())
            if key in cache:
                cached_value, cached_time = cache[key]
                if time.time() - cached_time < expiry_time:
                    return f"[CACHED] - {cached_value}"
            result = func(*args, **kwargs)
            cache[key] = result, time.time()
            return result

        return wrapper

    return decorator


@cached_with_expiry(expiry_time=5)  # Устанавливаем время кеширования 5 сек
def get_product(x, y):
    return x * y


print(get_product(23, 5))  # Вычисляем в первый раз
print(get_product(23, 5))  # Во второй раз срабатывает кеш
time.sleep(5)
print(get_product(23, 5))  # Кеш просрочился, поэтому вновь вычисляется значение
