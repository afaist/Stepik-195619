"""
    Напишите функцию get_info_about_object, которая принимает объект и выводит
    информацию обо всех его атрибутах и методах в следующем формате:

    сперва выводится список всех атрибутов и методов
    на следующей строке фраза «Всего у объекта {count} атрибутов и методов»

Примечание: тестирование на платформе будет производиться на версии Python
3.10, поэтому не переживайте, если вы используете у себя на устройстве другую
версию python и у вас не совпадает вывод.
"""


def get_info_about_object(obj):
    object = dir(obj)
    if "__type_params__" in object:
        object.remove("__type_params__")
    if "__getstate__" in object:
        object.remove("__getstate__")
    print(object)
    print(f"Всего у объекта {len(object)} атрибутов и методов")


# ------------------------ TEST -----------------------------
def print_goods(lst):
    for i in lst:
        print(i)


get_info_about_object(print_goods)
