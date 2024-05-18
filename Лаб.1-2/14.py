# Задача 14

# Написать функцию, которая принимает список строк.
# Функция должна вернуть случайный элемент списка в верхнем регистре

import random


lines = [
    "В янваpских снегах замеpзают pассветы",
    "Hа белых доpогах колдует пуpга",
    "И видится мне pаскаленное лето",
    "И pыжее солнце на желтых стогах",
]


def string_list(lines):
    return random.choice(lines).upper()


res = string_list(lines)
print(res)

# def string_list(lines):
#     print(random.choice(lines).upper())

# string_list(lines)