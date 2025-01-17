"""
    Напишите функцию concatenate(), которая принимает произвольное число
    именованных аргументов и объединяет их в одну большую строку без
    разделителей.

Вам необходимо написать только определение функции concatenate

Обратите внимание, что передаваемые значения могут быть различных типов данных
"""


def concatenate(**kwargs):
    return "".join(str(x) for x in kwargs.values())


print(concatenate(a="Я", b="Выучу", c="Этот", d="Питон", e="!"))
print(concatenate(first="i got ", second=5, third=" stars"))
print(concatenate(q="iHave", w="next", e="Coins", r=[10, 5, 10, 7]))
