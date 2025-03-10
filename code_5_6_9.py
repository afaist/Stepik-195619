"""
    Перед вами частично реализованная функция double_odd_numbers, которая принимает список чисел и возвращает в качестве результата новый список, составленный из нечетных чисел, увеличенных в два раза.

Внутри себя double_odd_numbers использует две функции:

    double, увеличивающая число в два раза;

    is_odd, проверяющая на нечетность

Ваша задача реализовать эти функции внутри  double_odd_numbers
"""


def double_odd_numbers(numbers):
    def double(x):
        return x * 2

    def is_odd(x):
        return x % 2 == 1

    return [double(x) for x in numbers if is_odd(x)]
