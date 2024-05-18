# Задача 10

# Написать функцию, которая принимает:
# 1) 1 обязательный аргумент дату в формате строки (можно использовать функцию из задачи №9)
# 2) 1 необязательный аргумент объект даты, по умолчанию должна быть текущая дата

# Функция должна вернуть число секунд между двумя этими датами.

from datetime import datetime
import random

y = random.randint(1995, 2004)  # год
m = random.randint(1, 12)  # месяц
d = random.randint(1, 31)  # день

d = datetime(y, m, d).date().strftime("%Y-%m-%d")
d_obj = datetime.today().strftime("%Y-%m-%d")


def seconds_between_dates(date, date_object=None):
    # Если аргумент объект даты не передается в функцию,то по умолчанию будет текущая дата
    if date_object == None:
        date_object = datetime.now()
    # Если аргумент объект даты  передается в функцию,то будет передаваться в формате строки
    else:
        date_object = datetime.strptime(date_object, "%Y-%m-%d")
    date = datetime.strptime(date, "%Y-%m-%d")
    return round((date_object - date).total_seconds())

# Если указана только дата
print(seconds_between_dates(d))
# Если указаны аругмент дата и объект дата
print(seconds_between_dates(d, d_obj))


# Обязательные аргументы – это аргументы, которые необходимо передать во время вызова функции с точным совпадением их позиций в вызове функции и определении функции.
