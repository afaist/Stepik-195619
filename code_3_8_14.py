"""
    Делаем короче

Напишите функцию truncate_sentences, которая обрезает предложения и оставляет
из них только первые N символов. Количество предложений, которые поступают на
вход функции, может быть произвольным
"""


def truncate_sentences(n, *texts):
    for text in texts:
        print(text[:n])


truncate_sentences(
    5,
    "Мой дядя самых честных правил,",
    "Когда не в шутку занемог,",
    "Он уважать себя заставил",
    "И лучше выдумать не мог.",
    "Его пример другим наука;",
    "Но, боже мой, какая скука",
    "С больным сидеть и день и ночь,",
    "Не отходя ни шагу прочь!",
)
