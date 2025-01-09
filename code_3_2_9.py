"""
    Самое длинное слово

Напишите функцию find_longest_word_len, которая принимает список слов и
возвращает длину самого длинного из них.
"""


def find_longest_word_len(words):
    return max(map(len, words))
