"""
    Выводим список покупок

Напишите функцию show_list, которая выводит список товаров из корзины (глобальная переменная shopping_list). У функции show_list есть необязательный логический параметр include_quantities, по умолчанию принимает значение True.

Если include_quantities имеет значение True, вы должны выводить имя товара и его количество в следующем формате:

{количество}x{имя_товара},

иначе необходимо вывести только имя.

Напишите только реализацию функции show_list
"""

shopping_list = {"Bread": 13, "Potato": 5, "Milk": 2, "Orange": 5}


def show_list(include_quantities=True):
    for key, value in shopping_list.items():
        if include_quantities:
            print(f"{value}x{key}")
        else:
            print(f"{key}")


show_list(True)
show_list(False)
