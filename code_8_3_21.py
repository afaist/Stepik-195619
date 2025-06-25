"""
    Проверка пароля

Ваша задача — создать сопрограмму check_password, которая проверяет поступающий
ей пароль на безопасность.

С точки зрения безопасности будет подходить пароль, для которого одновременно
выполняются следующие условия:

    длина не менее 10 символов;
    должна присутствовать хотя бы одна заглавная буква латинского алфавита;
    должна присутствовать хотя бы одна цифра;
    должен присутствовать хотя бы один служебный символ из набора !, @, #, $, %.

Пароли в виде строки поступают в сопрограмму при помощи метода send.
Сопрограмма должна порождать значение True, если пароль соответствует всем
перечисленным условиям, в противном случае - значение False.

Вам необходимо написать только определение функции-сопрограммы check_password.
"""

from collections.abc import Generator
from typing import NoReturn


def check_password() -> Generator[bool | None, str, NoReturn]:
    result: bool | None = None
    while True:
        password: str = yield result
        if len(password) < 10:
            result = False
        else:
            has_upper: bool = False
            has_digit: bool = False
            has_special: bool = False
            for char in password:
                if char.isupper():
                    has_upper = True
                elif char.isdigit():
                    has_digit = True
                elif char in "!@#$%":
                    has_special = True
            result = has_upper and has_digit and has_special
