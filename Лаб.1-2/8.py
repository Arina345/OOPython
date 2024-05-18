# Задача 8

# Написать программу, которая запрашивает у пользователя целое число больше 5.
# Так же программа должна сгенерировать число от 0 до 5.
# Оба числа должны быть переданы в функцию, созданную в задаче №7.
# На экран должен быть выведен результат работы функции.
# Дополнительно необходимо проверить введенное пользователем число

import random

number_one = int(input())

number_two = random.randint(0, 5)
# print(number_two)

# Решение в 7 строк

# def multiplication(a, b):
#     return a * b

# if number_one > 5 and number_one != 5:
#     res = multiplication(number_one, number_two)
#     print(res)
# else:
#     print("Введенное число меньше или равно 5")

# Решение в 3 строки

def multiplication(a, b):
    print(a*b if a > 5 else "Введенное число меньше или равно 5")

multiplication(a=number_one,b=number_two)