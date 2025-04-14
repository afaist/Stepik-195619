"""
    Валидация args - 2

Помните декоратор validate_all_args_str, который проверял, что все переданные
позиционные значения являются строками? А если вдруг нам потребуется создать
декоратор, который будет проверять аргументы не на принадлежность к строке, а,
скажем, к списку или числу? Тогда нам понадобится создавать отдельный декоратор
на каждый тип данных. Или сделать параметризированный декоратор
validate_all_args, который будет принимать тип данных в качестве аргумента и
проверять, что все значения в args относятся к переданному типу данных.

Ваша задача написать такой декоратор validate_all_args, который имеет параметр
type_. Если все позиционные аргументы принадлежат типу type_, то запускается
оригинальная функция; в противном случае необходимо отменить ее запуск и
вывести сообщение:

Все аргументы должны принадлежать типу {type_}
"""

from functools import wraps
from typing import Any
from collections.abc import Callable


def validate_all_args(
    type_: type,
) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            if not all(isinstance(arg, type_) for arg in args):
                print(f"Все аргументы должны принадлежать типу {type_}")
                return
            return func(*args, **kwargs)

        return wrapper

    return decorator
