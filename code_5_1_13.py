"""
    Запоминание результата

Представь, что ты работаешь в компании, которая занимается разработкой
программного обеспечения. Твой начальник дал тебе задание написать программу,
которая будет вычислять факториал числа. Факториал числа - это произведение
всех натуральных чисел от 1 до этого числа. Например, факториал числа 5 равен 1
* 2 * 3 * 4 * 5 = 120.

Однако, есть одно условие: ты должен сохранить результат вычисления факториала
в глобальной переменной, чтобы его можно было использовать в других частях
программы. Это означает, что значение факториала будет доступно для
использования в других функциях или блоках кода.

Также, твой начальник хочет, чтобы программа была оптимизирована и не вычисляла
факториал числа каждый раз заново. Вместо этого, программа должна проверять,
вызывалась ли уже функция с таким параметром. Если функция уже вызывалась с
таким параметром, то программа должна вернуть сохраненное значение, а не
вычислять его заново. Также перед возвратом такого значения функция должна
вывести на экран «Get from cache value factorial(n)»

Таким образом, твоя задача - написать функцию factorial, которая будет
вычислять факториал числа, сохранять результат в глобальной переменной и
проверять, вызывалась ли уже функция с таким параметром.
"""

facts = {}


def factorial(n: int) -> int:
    result = facts.get(n)
    if result:
        print(f"Get from cache value factorial({n})")
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        facts[n] = result
    return result


# --------------------------------------------------------
print(factorial(5))
print(factorial(6))
print(factorial(5))
