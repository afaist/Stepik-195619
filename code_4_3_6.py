"""
    Находим первый дубль

Напишите функцию get_first_repeated_word, которая имеет один параметр words -
список, состоящий из нескольких слов. Функция должна найти первый элемент,
который образует дубль с ранее стоящими элементами, и вернуть его в качестве
результата. Если передан список, в котором все слова различны, функция
get_first_repeated_word должна вернуть None
Регистр букв при сравнении нужно учитывать

Для функции  get_first_repeated_word  дополнительно нужно добавить

 1️⃣  док-строку  Находит первый дубль в списке

 2️⃣  аннотации при помощи модуля typing
"""

from typing import List, Optional


def get_first_repeated_word(words: List[str]) -> Optional[str]:
    "Находит первый дубль в списке"
    unique_words = set()
    for word in words:
        if word.lower() in unique_words:
            return word
        unique_words.add(word.lower())
    return None


# ----------------------- TEST -----------------------
print(get_first_repeated_word.__doc__)
print(get_first_repeated_word.__annotations__)
print(get_first_repeated_word(["hello", "hi", "hello"]))
print(get_first_repeated_word(["qwe", "qwer", "qwer", "qwe"]))
