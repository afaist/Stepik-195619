"""
    Поиск уровня

Создайте рекурсивную функцию find_level_element, которая определяет на каком
уровне вложенности располагается интересующий нас элемент. Нумерация уровней
вложенности начинается с единицы.

Функция find_level_element принимает некое значение value и список значений lst.

Функция find_level_element должна вернуть номер уровня, где встречается первое
найденное значение value в списке lst на любом уровне. Если же в lst
отсутствует значение value, функция find_level_element должна вернуть -1.
"""


def find_level_element(value, lst):
    if not lst:
        return -1
    if value in lst:
        return 1
    for item in lst:
        if isinstance(item, list):
            level = find_level_element(value, item)
            if level != -1:
                return level + 1
    return -1
