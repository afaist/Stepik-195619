"""
    Имеются три списка из 50 элементов: list_x, list_y и list_w

Ваша задача — произвести научные расчеты для соответствующих значений этих
списков. Нужно подставить в формулу

x2−x∗y∗w+w4x2−x∗y∗w+w4

поочередно первые значения из списков list_x, list_y и list_w, потом вторые,
затем третьи и т.д.  Значения из списка list_x должны подставляться в
переменную x, из списка list_y - в переменную y и из списка list_w - в
переменную w.

Всего должно получиться 50 вычисленных значений. Их необходимо сложить в список
и вывести на экран.
"""

list_x = [
    25,
    48,
    23,
    13,
    -18,
    -10,
    -3,
    16,
    2,
    -12,
    20,
    -14,
    14,
    45,
    41,
    6,
    11,
    15,
    22,
    -14,
    -11,
    41,
    15,
    48,
    47,
    41,
    -8,
    1,
    4,
    1,
    40,
    27,
    -11,
    -2,
    -14,
    -15,
    35,
    4,
    49,
    4,
    5,
    13,
    50,
    35,
    -3,
    3,
    30,
    -11,
    7,
    12,
]

list_y = [
    -9,
    17,
    41,
    47,
    -5,
    -10,
    -5,
    13,
    31,
    -11,
    37,
    9,
    46,
    27,
    -1,
    36,
    32,
    23,
    -12,
    38,
    8,
    9,
    17,
    16,
    29,
    -4,
    4,
    2,
    1,
    46,
    6,
    49,
    -16,
    21,
    -19,
    -10,
    15,
    -13,
    20,
    13,
    -18,
    21,
    -17,
    21,
    10,
    5,
    38,
    -1,
    18,
    22,
]

list_w = [
    9,
    -26,
    3,
    21,
    48,
    -14,
    43,
    -4,
    -16,
    16,
    41,
    43,
    -27,
    -9,
    10,
    -10,
    4,
    -2,
    1,
    7,
    30,
    -29,
    11,
    17,
    31,
    31,
    -26,
    38,
    38,
    -17,
    35,
    17,
    35,
    10,
    -25,
    42,
    -30,
    -10,
    -20,
    20,
    15,
    0,
    29,
    -30,
    -21,
    -13,
    -27,
    -21,
    -18,
    -26,
]

print(
    list(
        map(
            lambda x, y, w: x**2 - x * y * w + w**4,
            list_x,
            list_y,
            list_w,
        )
    )
)
