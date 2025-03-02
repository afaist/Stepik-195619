"""
    Результаты экзаменов - 3

Перепишите функцию print_results так, чтобы информация выводилась по убыванию оценок, а в случае их равенства предметы должны выводиться в алфавитном порядке без учета регистра
"""

marks = [
    ("English", 88),
    ("Science", 90),
    ("Maths", 88),
    ("Physics", 93),
    ("History", 78),
    ("French", 78),
    ("Art", 78),
    ("Chemistry", 88),
    ("Programming", 91),
]


def print_results(marks):
    for subject, mark in sorted(marks, key=lambda x: (-x[1], x[0].lower())):
        print(subject, mark)


print_results(marks)
