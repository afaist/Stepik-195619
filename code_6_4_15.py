"""
    Перед вами имеется реализация функции get_values

Ваша задача — избавиться от циклов for при помощи map и filter. Для этого
перепишите функцию get_values, но так, чтобы она не меняла свою изначальную
функциональность
"""


def get_values(nums: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(map(lambda x: x * 3, filter(lambda x: x % 3 == 0, nums)))
