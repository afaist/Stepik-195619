def decorator(func):
    def inner(*args, **kwargs):
        print("Стартуем декоратор")
        func(*args, **kwargs)
        print("Заканчиваем декоратор")

    return inner


@decorator
def say_hello_to(name, surname):
    print("hello", name, surname)


say_hello_to("Vasya", "Ivanov")


@decorator
def say_hello_to_all(*args):
    for name in args:
        print("Hello", name)


say_hello_to_all("Dima", "Andrei", "Pasha")
