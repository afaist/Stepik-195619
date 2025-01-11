"""
    Добавление в корзину покупок

Ваша задача написать функцию add_item, которая добавляет в корзину (глобальная
переменная shopping_list) товар и его количество.

Функция add_item обязательно должна принимать имя товара и необязательно - его
количество (по умолчанию оно равно 1)
"""

shopping_list = {}


def add_item(item, amount=1):
    global shopping_list
    shopping_list[item] = shopping_list.get(item, 0) + amount
