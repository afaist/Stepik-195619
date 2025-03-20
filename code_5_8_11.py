"""
    Функция count_calls

В этом задании вам нужно сделать функцию-замыкание count_calls, которая
подсчитывает сколько раз она была вызвана. Особенность этого замыкания
заключается в том, что количество вызовов должно храниться в атрибуте
total_calls.
"""


def count_calls():
    def inner():
        inner.total_calls += 1

    inner.total_calls = 0
    return inner


counter = count_calls()
counter()
counter()
print(counter.total_calls)
counter()
print(counter.total_calls)
