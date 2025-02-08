"""
    Напишите функцию rotate , которая имеет следующие параметры

    ✔️  lst - список чисел (целых или вещественных)

    ✔️  shift - целое число, обозначающее сдвиг. По умолчанию равен 1

Функция rotate должна выполнить циклический сдвиг элементов списка на shift
позиций и вернуть в качестве ответа новый список со смещенными значениями. Если
значение shift положительно, сдвиг необходимо производить вправо, если
отрицательно — влево.

На картинке ниже показан результат циклического сдвига элементов списка на
единицу влево (источник картинки)

Дополнительные условия для задания:

    1️⃣ Функция rotate  должна быть чистой

    2️⃣ необходимо проаннотировать параметры функции rotate  и ее возврат без
      использования модуля typing. Для тестов важен порядок следования типов

    3️⃣ добавьте док-строку с содержанием «Функция выполняет циклический сдвиг
      списка на shift позиций вправо(shift>0) или влево(shift<0)»
"""


def rotate(lst: list[int | float], shift: int = 1) -> list[int | float]:
    "Функция выполняет циклический сдвиг списка на shift позиций вправо(shift>0) или влево(shift<0)"
    shift = shift % len(lst)
    new_lst = lst[-shift:] + lst[:-shift]
    return new_lst


# -------------------- TEST --------------------
lst = [1, 2, 3, 4, 5]
print(lst)
shift = 2
print("shift = ", shift)
print(rotate(lst, shift))
print(rotate.__doc__)
print(rotate.__annotations__)
shift = -10
print("shift = ", shift)
print(rotate([1, 2, 3, 4, 5, 6], shift))
