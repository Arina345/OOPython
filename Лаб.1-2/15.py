# Задача 15

# Написать функцию, которая примет произвольную строку.
# Функция должна вернуть словарь, который содержит в  себе следующие ключи и значения:

# 1) length — длина строки
# 2) words_count — количество слов
# 3) digit_count — количество цифровых символов


s = "словари – изменяемые коллекции элементов с произвольными индексами – ключами "

l = len(s)
w_c = 0
d_c = 0
s = s.split(" ")
print(s)

for i in s:
    if i.isalpha() == True:
        w_c += 1
    if i.isdigit() == True:
        d_c += 1


# def stroka(s):
#    return l, w_c, d_c

# my_dict = {"length ": l, "words_count": w_c, "digit_count": d_c}
# print(my_dict)


def stroka(s,l, w_c, d_c):
    print({"length ": l, "words_count": w_c, "digit_count": d_c})

stroka(s,l, w_c, d_c)

# isalpha() - проверяет состоит ли строка только из букв
# isdigit()  - проверяет состоит ли строка только из цифр