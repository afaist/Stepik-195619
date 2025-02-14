"""
    Обменный пункт

Одной из базовых банковских услуг является обмен валют.

Напишите функцию convert, которая умеет конвертировать доллар в другую валюту и
наоборот. Для конвертации используются текущие курсы валют, которые хранятся в
глобальном словаре exchange_rates.

Результат округлите до двух знаков после запятой при помощи функции round
"""

exchange_rates = {
    "USD": 1.0,
    "EUR": 0.861775,
    "GBP": 0.726763,
    "INR": 75.054725,
    "AUD": 1.333679,
    "CAD": 1.237816,
    "SGD": 1.346851,
}


def convert(currency_to: str, currency_from: str, value: int) -> float:
    return round(value * exchange_rates[currency_from] / exchange_rates[currency_to], 2)


# -------------------------------------------------------------------------------
currency = convert("USD", "EUR", 100)
print(currency)
currency = convert("EUR", "USD", 100)
print(currency)
