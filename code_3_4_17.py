"""
    Резервация столов: изменение требований - 2

    Продолжение задачи «Резервация столов: изменение требований»

Помните у нас была реализована функция reserve_table ? Она принимала три
обязательных значения: номер стола, имя клиента и статус VIP.

Как только менеджеры узнали про параметр со значением по умолчанию они сразу
решили попросить вас переписать функцию reserve_table так, чтобы статус VIP
клиента был по умолчанию равен False. Потому что большинство клиентов не так
часто заходят в данное заведение и по статистике больше обычных клиентов,
нежели вип-персон.
"""

tables = {
    1: {"name": "Andrey", "is_vip": True},
    2: None,
    3: None,
    4: None,
    5: {"name": "Vasiliy", "is_vip": False},
    6: None,
    7: None,
    8: None,
    9: {"name": "Misha", "is_vip": False},
}


def is_table_free(table_number):
    return tables[table_number] is None


def reserve_table(table, name, is_vip=False):
    if is_table_free(table):
        tables[table] = {"name": name, "is_vip": is_vip}


def delete_reservation(table):
    tables[table] = None
