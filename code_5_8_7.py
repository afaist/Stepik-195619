"""
    Функция make_repeater

Ваша задача создать функцию-замыкание make_repeater, которая должна дублировать
переданную в нее строку N раз. При создании замыкания передается число N -
количество для повторения.
"""

from collections.abc import Callable


def make_repeater(count: int) -> Callable[[str], str]:
    def repeater(string: str) -> str:
        return string * count

    return repeater
