"""
Делаем заказ в ресторане - часть 2

    Вам потребуется код из следующих задач

        ✔  «Делаем заказ в ресторане»

        ✔  «Удаляем заказ»

Проблема предыдущей версии функции make_order заключается в том, что она перезатирала ранее заказанные блюда. И она также не давала в рамках одного вызова заказать несколько блюд из одной категории.

Ваша задача переписать функцию  make_order так, чтобы она сохраняла блюда из одной категории в виде списка, а в случае нового заказа с блюдами из той же категории, эти блюда добавлялись бы в тот же список..

Давайте разберем примеры, имеется такая структура данных

tables = {
    1: {'name': 'Andrey', 'is_vip': True, 'order': {}},
    2: None,
    3: {'name': 'Vasiliy', 'is_vip': False, 'order': {}},
}

Далее Андрей делает два заказа make_order

make_order(1, soup='Borsh')
make_order(1, soup='Лапша')

Оба заказанных блюда из категории суп, значит в итоге нужно сложить их в один список и получить следующее

{
 1: {'name': 'Andrey', 'is_vip': True, 'order': {'soup': ['Borsh', 'Лапша']}},
 2: None,
 3: {'name': 'Vasiliy', 'is_vip': False, 'order': {}}
}

Также новая реализация функции make_order   должна позволять передать несколько блюд через запятую в рамках одной категории

make_order(1, soup='Borsh,Лапша', desert='Медовик', drink='Cola')
make_order(1, soup='Гаспачо', desert='Печенье,Наполеон')



Для успешного решения задания вам необходимо переписать функцию make_order и продублировать ранее созданные reserve_table и delete_order со всеми их зависимостями.

Не забывайте про кнопку «Запустить код» для проверки работоспособности программы перед отправкой.
Удаляем заказ

    Вам потребуется код из задачи «Делаем заказ в ресторане»

От менеджеров поступило требование написать функционал, который позволяет
очищать заказ. Для этого нужно разработать функцию delete_order, которая имеет
следующие параметры
"""

tables = {
    1: {"name": "Andrey", "is_vip": True, "order": {}},
    2: None,
    3: None,
    4: None,
    5: {"name": "Vasiliy", "is_vip": False, "order": {}},
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
            tables[table]["order"][item] = tables[table]["order"].get(
                item, []
            ) + kwargs[item].split(",")


def delete_order(*, number_table, delete_all=False, **kwargs):
    order = tables[number_table]["order"]
    if delete_all:
        tables[number_table]["order"] = {}
    else:
        for item in kwargs:
            if kwargs[item] and item in order:
                del order[item]


# -------------------- TEST------------------------------
make_order(1, soup="Borsh,Лапша", desert="Медовик", drink="Cola")
make_order(1, soup="Гаспачо", desert="Печенье,Наполеон")

reserve_table(2, "Vlad")

make_order(2, soup="Чечевичный", salad="Цезарь,Мимоза", breakfast="Яичница,Бекон")
make_order(2, drink="Raf,Coffee,Juice", main_dish="Утка по-пекински,Отбивная")
make_order(2, desert="Трюфель", call="такси")

make_order(1, desert="Наполеон", drink="Чай", meal="Манка,Овсянка")
make_order(1, desert="Вишня", drink="Кофе")
print(tables)
delete_order(
    number_table=2, drink=True, desert=True, call=True, шаурма=True, cheesecake=True
)
delete_order(number_table=1, soup=True, desert=True, call=True)
print(tables)
