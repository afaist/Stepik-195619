"""
    Поиск во вложенном списке

Ранее мы уже делали проверку на вхождение элемента в линейный список. Теперь
ваша задача переписать функцию is_member так, чтобы она могла искать элемент в
списке с произвольной вложенностью.

Функция принимает некое значение value и список значений lst.

Функция is_member должна вернуть True, если значение value присутствует в
списке lst на любом уровне, и False в противном случае.
"""


def is_member(value, lst: list) -> bool:
    if value in lst:
        return True
    for item in lst:
        if isinstance(item, list):
            if is_member(value, item):
                return True
    return False
