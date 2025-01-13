"""
Перепишите функцию my_func так, чтобы она стала чистой
"""


def my_func(collection, n):
    new_collection = collection.copy()
    for i in range(1, n + 1):
        new_collection.append(i)
    return new_collection
