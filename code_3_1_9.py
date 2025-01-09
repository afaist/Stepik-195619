"""
    Количество високосных лет

Напишите функцию count_leap_years, которая принимает два года y1 и y2, причем y1 <= y2, и возвращает количество високосных лет в промежутке от y1 включительно до  y2 не включительно.

При реализации функции count_leap_years используйте ранее созданную функцию is_leap.

Напишите только определения необходимых функций.
"""


def is_leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def count_leap_years(y1, y2):
    count = 0
    for year in range(y1, y2):
        if is_leap(year):
            count += 1
    return count
