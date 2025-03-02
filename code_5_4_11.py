"""
Результаты экзаменов - 2

Перепишите функцию print_results так, чтобы информация выводилась по убыванию
оценок.

В случае равенства оценок предметы должны выводиться на экран в том же порядке,
в котором они следовали во входном списке
"""


def print_results(results):
    results = sorted(results, key=lambda x: -x[1])
    for item in results:
        print(*item)


# -----------------------TEST-----------------------
marks = [
    ("English", 88),
    ("Science", 90),
    ("Maths", 97),
    ("Physics", 93),
    ("History", 82),
]
print_results(marks)
