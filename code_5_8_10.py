"""
    Обратный отсчет

Напишите функцию-замыкание countdown, которая будет вести обратный отсчёт от
переданного числа N до нуля. После того как замыкание будет вызвано более N
раз, необходимо выводить сообщение «Превышен лимит, вы вызвали более N раз»
"""

from collections.abc import Callable


def countdown(n: int) -> Callable[[], None]:
    def inner():
        nonlocal n
        if n > 0:
            print(n)
            n -= 1
            inner()
        else:
            print("Превышен лимит, вы вызвали более N раз")

    return inner
