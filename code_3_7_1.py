"""
Вспоминаем про функцию print_person_info. Вместо трех параметров name, age,
company создадим один параметр **kwargs, который нам позволит принимать
произвольное количество именованных аргументов. Теперь мы можем
распаковывать словари различной длины в момент вызова функции и/или
передавать именованные аргументы
"""


def print_person_info(**kwargs):
    print("=" * 20, "Person Info", "=" * 20)
    pairs = [f"{k} = {v}" for k, v in kwargs.items()]
    print(", ".join(pairs))


bob = {"name": "Bob", "age": 42, "company": "Google"}
print_person_info(**bob)
artem = {"name": "Artem", "age": 25, "company": "Yandex", "hobby": "soccer"}

print_person_info(last_name="Petrov", name="Artem", music=["rock", "rap", "Indi"])
print_person_info(lastname="Egorov", **bob)
