"""
    Лучшая оценка - 2

 Усовершенствуйте функцию get_info_marks из предыдущего урока так, чтобы она
 возвращала словарь, в котором для каждого студента формируется словарь,
 хранящий информацию как о лучшей оценке студента(ключ «best»), так и худшей
 (ключ «worst»)

Параметры функции остаются неизменными.
"""


def get_info_marks(students, *marks):
    return {
        student: {"best": max(mark), "worst": min(mark)}
        for student, mark in zip(students, zip(*marks))
    }
