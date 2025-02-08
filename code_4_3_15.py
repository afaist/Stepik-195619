"""
    Шифр цезаря

На основании функции rotate_letter из предыдущего задания мы с вами можем
реализовать знаменитый шифр Цезаря. Этот шифр берет каждую букву исходной фразы
и смещает ее на значение ключа. Под ключом здесь подразумевается значение
сдвига shift. В пределах кодирования одной фразы значение сдвига всегда
постоянно.

И так, ваша задача создать функцию caesar_cipher, которая имеет два
обязательных параметра:

     1️⃣ phrase входной текст для шифрования

     2️⃣ key значение ключа шифра, он же сдвиг.

Внутри функции caesar_cipher  необходимо последовательно пройтись по каждому
символу и преобразовать его по следующим правилам:

    если символ является знаком пунктуации, оставляем его как есть
    если это буква, то сместить ее при помощи ранее написанной функции rotate_letter  на значение ключа

Закодированный текст необходимо вернуть в качестве ответа. Вот пример работы

caesar_cipher('leave out all the rest', -1) => 'kdzud nts zkk sgd qdrs'
caesar_cipher('one more light', 3) => 'rqh pruh oljkw'

Для успешного решения напишите реализацию функции caesar_cipher, которая
использует функцию rotate_letter. (нужно продублировать определение функции
rotate_letter из предыдущего урока).

Дополнительно нужно :

     ✔️  сделать аннотацию параметров и возвращаемого значения всех функций

     ✔️  сделать док-строку для функции caesar_cipher со значением «Шифр Цезаря»
"""


def rotate_letter(letter: str, shift: int) -> str:
    "Функция сдвигает символ letter на shift позиций"
    return chr((ord(letter) - ord("a") + shift) % 26 + ord("a"))


def caesar_cipher(phrase: str, key: int) -> str:
    "Шифр Цезаря"
    return "".join(
        rotate_letter(char, key) if char.isalpha() else char for char in phrase
    )


# -------------------------TEST---------------------------------------------
print(caesar_cipher.__annotations__)
print(caesar_cipher.__doc__)
assert caesar_cipher("leave out all the rest", -1) == "kdzud nts zkk sgd qdrs"
assert caesar_cipher("one more light", 3) == "rqh pruh oljkw"
assert caesar_cipher("from the inside", 10) == "pbyw dro sxcsno"
