"""
   В переменную starts_with присвойте lambda функцию, которая принимает строку
   и возвращает True, когда переданная строка начинается с буквы «W». Во всех
   остальных случаях нужно возвращать False

Ничего кроме создания переменной starts_with делать не нужно
"""

starts_with = lambda s: s.startswith("W")

# --------------------------------------------------------------------------
print(starts_with("WORLD"))
print(starts_with("world"))
print(starts_with("Hello"))
print(starts_with("World!"))
print(starts_with.__name__)
