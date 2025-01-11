"""
Исправьте функции так, чтобы добавление одной оценки студенту не влияло на
оценки других учеников
"""


def create_student(name, age, marks=None):
    return {
        "name": name,
        "age": age,
        "marks": [] if marks is None else marks,  # оценки
    }


def add_mark(student, mark):
    student["marks"].append(mark)


ivan = create_student("Ivan", 15)
print(ivan)
anatoliy = create_student("Anatoliy", 16)
print(anatoliy)

add_mark(ivan, 5)
add_mark(ivan, 5)
add_mark(anatoliy, 3)
add_mark(anatoliy, 4)
print(ivan)
print(ivan["marks"])
print(anatoliy)
print(anatoliy["marks"])
