"""
    Нахождение среднего арифметического

Ваша задача — создать корутину get_average, которая накапливает среднее
арифметическое переданных в нее чисел.

Числа поступают в корутину при помощи метода send, корутина должна порождать
текущее накопленное значение среднего арифметического.

Вам необходимо написать только определение функции-корутины get_average.
"""

from typing import Generator, NoReturn


def get_average() -> Generator[float | None, int, NoReturn]:
    """Возвращает накопленное среднее значение переданных чисел

    Yields:
        Возвращает float | None
        Получает int
        Финальное значение не возвращает (NoReturn)
    """
    numbers: list[int] = []
    while True:
        number = yield sum(numbers) / len(numbers) if numbers else None
        numbers.append(number)
