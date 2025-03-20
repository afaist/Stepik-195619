"""
    Замыкание-аккумулятор

Ваша задача создать функцию-замыкание create_accumulator, которая должна
накапливать (суммировать) внутри себя все значения, которые ей будут переданы.
При создании замыкания стартовая сумма должна быть равна нулю. Посмотрите
пример ниже:

summator_1 = create_accumulator()
print(summator_1(1)) # печатает 1
print(summator_1(5)) # печатает 6
print(summator_1(2)) # печатает 8

summator_2 = create_accumulator()
print(summator_2(3)) # печатает 3
print(summator_2(4)) # печатает 7

При каждом вызове должна возвращаться накопленная сумма, которая хранится в
замыкании.

Обратите внимание, что объекты из примера summator_1 и summator_2 хранят и
накапливают свои собственные суммы.

Необходимо только определить функцию-замыкание create_accumulator, остальное мы
сделаем за вас
"""

from collections.abc import Callable


def create_accumulator(n: int | float = 0) -> Callable[[int | float], int | float]:
    def accumulator(x: int | float) -> int | float:
        nonlocal n
        n = n + x
        return n

    return accumulator
