"""
Напишите функцию filter_words, которая принимает список строк и возвращает
новый список, который состоит из строк, длина которых четыре символа, или
начинающихся на заглавную букву S.
"""


def filter_words(words: list[str]) -> list[str]:
    return list(filter(lambda x: len(x) == 4 or x.startswith("S"), words))
