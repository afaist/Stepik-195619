"""
Перед вами реализация двух функций-декораторов  first_validator и
second_validator.

Также имеется функция sum_values.

Вам необходимо сперва проанализировать имеющийся код и разобраться, как он
работает.

После этого вашей задачей является:

   ✔️ наложить два декоратора на функцию sum_values в правильной
   последовательности;

   ✔️ вызвать задекорированную функцию sum_values подобрав аргументы так, чтобы
   совпал вывод результата.

Код самих функций менять не нужно.
"""


def first_validator(func):
    def my_wrapper(*args, **kwargs):
        print("Начинаем важную проверку")
        if len(args) == 3:
            func(*args, **kwargs)
        else:
            print("Важная проверка не пройдена")
            return None
        print("Заканчиваем важную проверку")

    return my_wrapper


def second_validator(func):
    def my_wrapper(*args, **kwargs):
        print("Начинаем самую важную проверку")
        if kwargs.get("name") == "Boris":
            func(*args)
        else:
            print("Самая важная проверка не пройдена")
            return None
        print("Заканчиваем самую важную проверку")

    return my_wrapper


@second_validator
@first_validator
def sum_values(*args):
    print(f"Получили результат равный {sum(args)}")


sum_values(7, 50, 20, name="Boris")
