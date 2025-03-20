"""
Замыкание
"""


def main_func():
    name = "Vladimir"

    def inner_func():
        print(name)

    return inner_func


f = main_func()
print(f.__name__)
f()
f()


def adder(start_value):
    def inner(income):
        print(
            f"start value: {start_value}, income: {income}"
        )  # print(start_value, income)
        return start_value + income

    return inner


add_from_2 = adder(2)
add_from_7 = adder(7)
print(add_from_2.__name__)
print(add_from_2(5))
print(add_from_2(3))

print(add_from_7(4))
print(add_from_7(9))

print("Счетчик вызовов функции")


def counter():
    count = 0

    def inner():
        nonlocal count
        count += 1
        return count

    return inner


q = counter()
r = counter()
print(q())
q()
print(q())
print(r())
