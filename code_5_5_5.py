"""
    Напишите функцию create_attrs, которая принимает объект obj и список
    кортежей. Каждый кортеж состоит из пары значений: имя атрибута в виде
    строки и его будущее значение.

Задача функции create_attrs — создать на основании внутренних кортежей списка
новые атрибуты к переданному объекту.

Для проверки работоспособности программы скопируйте реализацию функции
check_exist_attrs из предыдущего задания
"""


def check_exist_attrs(obj: object, attrs: list[str]) -> dict[str, bool]:
    return {attr: hasattr(obj, attr) for attr in attrs}


def create_attrs(obj: object, attrs: list[tuple[str, str]]) -> None:
    for attr, value in attrs:
        setattr(obj, attr, value)


def print_goods(lst):
    pass


create_attrs(print_goods, [("house", 1), ("level", 3), ("cost", 1000000)])
print(print_goods.house)
print(print_goods.level)
print(print_goods.cost)
