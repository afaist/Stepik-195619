"""
    Проверка на вхождение через рекурсию

Перепишите реализацию функции is_member через рекурсию. Напоминаю, функция
is_member  должна проверять, есть ли значение value в линейном списке lst.

Функция is_member должна вернуть True, если значение value присутствует в
списке lst, и False в противном случае.

Гарантируется, что список lst не будет вложенным
"""


def is_member(value: int | str | float, lst: list[int | str | float]) -> bool:
    if lst == []:
        return False
    else:
        if lst[0] == value:
            return True
        else:
            return is_member(value, lst[1:])
