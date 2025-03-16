"""
    Фильтрация - 2

На основании предыдущей функции filter_list, напишем новую функцию
filter_collection. Особенность функции filter_collection заключается в том, что
она возвращает тот же тип коллекции, который она принимала на вход.

А остальной принцип  ее работы похож с функцией filter_list: обе принимают
функцию f для проверки, при помощи которой фильтруются элементы коллекции

Функция f обязательно должна проверять определенное условие и возвращать булев
тип.
"""


def filter_collection(f, collection):
    result = [i for i in collection if f(i)]
    type_collection = type(collection)
    if type_collection is str:
        return "".join(result)
    elif type_collection is list:
        return result
    else:
        return type_collection(result)


def is_even(num):
    return num % 2 == 0


numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
even_numbers = filter_collection(is_even, numbers)
print(even_numbers)


def is_positive(num):
    return num > 0


numbers = [-1, 2, -3, 4, 5, -6, 7, -8, -9, 10]
positive_numbers = filter_collection(is_positive, numbers)
print(positive_numbers)
print(
    filter_collection(lambda x: x not in "aeiou", "I never heard those lyrics before")
)
