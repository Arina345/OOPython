# Задача 2

# Написать программу, которая должна поочередно запросить у пользователя его ФИО и вывести результат в формате «Фамилия И. О.»

name, surname, patronymic = input(), input(), input()

#print(f"{surname} {name[0]}.{patronymic[0]}.")

print('{} {}. {}.'.format(surname,name[0],patronymic[0]))
