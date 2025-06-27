"""
Вновь словарь

На предыдущем уроке вы решали задачу «Словарь».  В ней гарантировалось, что в
сопрограмму alphabet будут передаваться только значения, которые являются
ключами глобальной переменной DICTIONARY.

Теперь вам необходимо переписать сопрограмму alphabet  так, чтобы она могла
обрабатывать исключение KeyError. В  случае, когда возникнет исключение
KeyError, сопрограмма должна генерировать значение «default».



Переменная DICTIONARY вам в редакторе кода по-прежнему не видна, но вы можете
обращаться к ней внутри сопрограммы alphabet."""

from collections.abc import Generator
from typing import Any


DICTIONARY = {
    "a": "apple",
    "b": "banana",
    "c": "cat",
    "d": "dog",
    "e": "elephant",
    "f": "fox",
    "g": "gorilla",
    "h": "hippo",
    "i": "iguana",
    "j": "jaguar",
    "k": "koala",
    "l": "llama",
    "m": "monkey",
    "n": "newt",
    "o": "octopus",
    "p": "parrot",
    "q": "quail",
    "r": "rabbit",
    "s": "squirrel",
    "t": "tiger",
    "u": "unicorn",
    "v": "viper",
    "w": "walrus",
    "x": "xenomorph",
    "y": "yak",
    "z": "zebra",
}


def alphabet() -> Generator[str | None, str | Any, str]:
    letter = yield
    while True:
        try:
            letter = yield DICTIONARY.get(letter, "default")
        except KeyError:
            letter = yield "default"
