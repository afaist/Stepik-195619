"""
ефакторинг rotate

Перепишите функцию rotate так, чтобы она стала работать не со списками, а с
кортежами. Для этого выполните следующие шаги:

    1️⃣ переименовать параметр lst - в tpl. Теперь функция будет принимать не
      список, а кортеж целых или вещественных чисел

    2️⃣ изменится тип возвращаемого значения. Вместо списка функция rotate теперь
      должна возвращать кортеж. Остальная логика программы не меняется

    3️⃣ док строку изменить на «Функция выполняет циклический сдвиг кортежа на
      shift позиций вправо (shift>0) или влево (shift<0)»
"""


def rotate(tpl: tuple[int | float, ...], shift: int = 1) -> tuple[int | float, ...]:
    "Функция выполняет циклический сдвиг кортежа на shift позиций вправо (shift>0) или влево (shift<0)"
    shift = shift % len(tpl)
    new_tpl = tpl[-shift:] + tpl[:-shift]
    return new_tpl


# -------------------- TEST --------------------
tpl = (1, 2, 3, 4, 5)
print(tpl)
shift = 2
print("shift = ", shift)
print(rotate(tpl, shift))
print(rotate.__doc__)
print(rotate.__annotations__)
shift = -10
print("shift = ", shift)
print(rotate((1, 2, 3, 4, 5, 6, 7), shift))
shift = 21
print(rotate((1, 2, 3, 4, 5, 6, 7), shift))
