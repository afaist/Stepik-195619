"""
    Проверка на палиндром

Определите функцию is_palindrome, которая принимает строку и отвечает на
вопрос, является ли она палиндромом или нет

    Палиндромами считаются слова, которые читаются одинаково слева направо и справа налево, как например слово «радар»

При проверке не нужно учитывать регистр букв. Это значит, что слова «радар» и
«Радар» считаются одинаковыми.

Также во входной строке могут встречаться пробелы, их необходимо исключить из
проверки. Остальные знаки пунктуации, такие как запятые, точки, дефисы и т.д.,
во входных данных отсутствуют.
"""


def is_palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]
