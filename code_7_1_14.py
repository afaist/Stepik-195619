"""
Какова глубина рекурсии в следующем коде?
"""


def my_recursive_func(value):
    if len(value) <= 10:
        print(value)
        my_recursive_func(2 * value)


my_recursive_func("!")
