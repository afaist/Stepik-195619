"""
Удаляем заказ

    Вам потребуется код из задачи «Делаем заказ в ресторане»

От менеджеров поступило требование написать функционал, который позволяет
очищать заказ. Для этого нужно разработать функцию delete_order, которая имеет
следующие параметры

    обязательный ключевой параметр number_table - номер стола, где будем
    очищать заказ

    необязательный ключевой параметр delete_all со значением по умолчанию
    False. Если передать в него True, должна очищаться полностью информация о
    заказе для указанного столика. При значении False удаление в заказе будет
    точечным по категориям

    произвольное количество ключевых параметров с булевым значением вида

    drink=True, desert=True, call=True, шаурма=True

    Среди этих значений вам нужно удалять из заказа только те, имена которых
    находятся в списке категорий и переданное значение равно True

Для успешного решения задания вам необходимо определить новую функцию
delete_order  и продублировать ранее созданные reserve_table и make_order со
всеми их зависимостями.
"""

tables = {
    1: {"name": "Andrey", "is_vip": True, "order": {"soup": "Borsh"}},
    2: None,
    3: {"name": "Vasiliy", "is_vip": False, "order": {}},
}

categories = {"salad", "soup", "main_dish", "drink", "desert"}


def is_table_free(table_number):
    return tables[table_number] is None


def reserve_table(table, name, is_vip=False):
    if is_table_free(table):
        tables[table] = {"name": name, "is_vip": is_vip, "order": {}}


def delete_reservation(table):
    tables[table] = None


def make_order(table, **kwargs):
    for item in kwargs:
        if item in categories:
            tables[table]["order"][item] = kwargs[item]


def delete_order(*, number_table, delete_all=False, **kwargs):
    order = tables[number_table]["order"]
    if delete_all:
        tables[number_table]["order"] = {}
    else:
        for item in kwargs:
            if kwargs[item] and item in order:
                del order[item]


# -------------------- TEST------------------------------
make_order(1, soup="Borsh")
make_order(1, soup="Лапша", bring="Салфетку", meal="Манка")
make_order(1, soup="Borsh")
make_order(1, soup="Лапша", bring="Салфетку", meal="Манка")

reserve_table(2, "Vlad")

make_order(2, soup="Чечевичный", salad="Цезарь", breakfast="Яичница")
make_order(2, drink="Raf", main_dish="Утка по-пекински")
make_order(2, desert="Трюфель", call="такси")
print(tables)
try:
    delete_order(1, delete_all=True)
except TypeError:
    print("Вызов delete_order без передачи значения по ключу не должен проходить")
else:
    raise ValueError("Проверьте типы параметров функции delete_order")
delete_order(
    number_table=2, drink=True, desert=True, call=True, шаурма=True, cheesecake=True
)
delete_order(number_table=1, soup=True, desert=True, call=True)
print(tables)
