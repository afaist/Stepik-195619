"""
    Декоратор uppercase_elements

Ваша задача написать логику работы декоратора uppercase_elements, который умеет
работать с функциями, возвращающими коллекции элементов. Задача декоратора
uppercase_elements преобразовать каждый строковый элемент коллекции к
заглавному регистру. В случае, если оригинальная функция возвращает словарь, то
элементом считаем только строковые ключи словаря.

Элементы, не являющиеся строкой, не должны изменяться декоратором
uppercase_elements

Гарантируется, что коллекции, возвращаемые оригинальной функцией, не являются
вложенными
"""


def uppercase_elements(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if type(result) is list:
            return [str(x).upper() if type(x) is str else x for x in result]
        if type(result) is dict:
            return {
                key.upper() if type(key) is str else key: value
                for key, value in result.items()
            }

    return wrapper
