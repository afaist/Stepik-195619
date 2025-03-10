"""
    Напишите функцию check_exist_attrs, которая принимает объект obj и список
    строк, в котором хранятся имена атрибутов.

Функция check_exist_attrs должна вернуть словарь, в котором ключами будут
являться имена атрибутов из переданного списка. Напротив каждого ключа должно
быть булево значение: True, если атрибут присутствует в объекте obj , в
обратном случае - False.

Ключи в итоговом словаре необходимо создавать в порядке следования имен
атрибутов во входном списке
"""


def check_exist_attrs(obj: object, attrs: list[str]) -> dict[str, bool]:
    return {attr: hasattr(obj, attr) for attr in attrs}


def print_goods(lst):
    pass


print_goods.is_working = False
print_goods.status = "Not ready"

print(check_exist_attrs(print_goods, ["is_working", "status", "time", "speed"]))
