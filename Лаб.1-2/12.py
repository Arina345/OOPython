# Задача 12

# Написать программу, которая переведет введенное пользователем число от -5 до 5 в значение словами. Например, «минус один»

# Дополнительно необходимо проверить введенное пользователем число.

num = int(input())

my_dict = {
    -1: "минус один",
    -2: "минус два",
    -3: "минус три",
    -4: "минус четыри",
    -5: "минус пять",
    0: "ноль",
    1: "один",
    2: "два",
    3: "три",
    4: "четыри",
    5: "пять",
}

result = my_dict.get(num, "Введеное число не принадлежит интервалу от -5 до 5")
print(result)
# if num in range(-5, 5 + 1):
#     for key, value in my_dict.items():
#         if num == key:
#             print(value)
# else:
#     print("Введеное число не принадлежит интервалу от -5 до 5")
