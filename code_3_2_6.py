"""
    Фильтрация слов

Напишите функцию filter_long_words, которая принимает список слов и целое число
N и возвращает список слов, длина которых больше чем число N

"""


def filter_long_words(words, n):
    return [word for word in words if len(word) > n]
