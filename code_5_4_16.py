"""
   Сортировка товаров

Напишите функцию print_goods, которая принимает список словарей. В самих
словарях хранится информация о товарах: имя, модель и цвет. Задача функции
print_goods вывести на экран информацию о товарах  в следующем формате

Производитель: <make>, модель: <model>, цвет: <color>

при этом товары должны быть отсортированы по цвету в лексикографическом порядке
(по алфавиту) без учета регистра и по убыванию модели (второй критерий
сортировки)
"""

models = [
    {"make": "Nokia", "model": 216, "color": "Black"},
    {"make": "Mi Max", "model": 2, "color": "Gold"},
    {"make": "Samsung", "model": 7, "color": "Blue"},
    {"make": "Apple", "model": 10, "color": "Silver"},
    {"make": "Oppo", "model": 9, "color": "Red"},
    {"make": "Huawei", "model": 4, "color": "Grey"},
    {"make": "Honor", "model": 3, "color": "Black"},
]


def print_goods(models):
    for good in sorted(models, key=lambda x: (x["color"].lower(), -x["model"])):
        print(
            f"Производитель: {good['make']},",
            f"модель: {good['model']},",
            f"цвет: {good['color']}",
        )


print_goods(models)
