def my_func(first, second, third):
    print("--" * 30)
    print("Адреса локальных переменных:")
    first = 200
    second[1] = 999
    third["Hello"] = "Hello world"
    print(first, id(first))
    print(second, id(second))
    print(third, id(third))


a = 100
b = [10, 20, 30]
c = {"Hello": "Привет"}

print("Адреса глобальных переменных:")
print(f"{a=}", id(a))
print(f"b={b}", id(b))
print(f"c={c}", id(c))

my_func(a, b, c)
print("--" * 30)
print("Адреса глобальных переменных:")
print(f"{a=}", id(a))
print(f"b={b}", id(b))
print(f"c={c}", id(c))
