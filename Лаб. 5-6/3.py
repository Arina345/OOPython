# Определить метод get_len для вычисления длины отрезка. Длина отрезка
# вычисляется следующим образом: (формула)

# Определить метод приведения к строке. Пример: AB(xa, ya; xb, yb)

# Определить метод сложения двух отрезков таким образом, чтобы возвращался новый экземпляр класса BrokenLine.

from one import Point, BrokenLine
from math import sqrt


def get_len(self, other):
    D = sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)
    return f"Длина отрезка: {round(D)}"


def __str__(self, other):
    return f"{self.n}{other.n}({self.x}a, {self.y}a; {other.x}b, {other.y}b)"


# Функция zip () используется для совмещения двух и более списков в один.
# Она возвращает итератор кортежей, где i-ый кортеж содержит i-ый элемент из каждого из переданных списков.


def __add__(self, other):
    res = self.list + other.list
    return BrokenLine(res)
    # return BrokenLine(a + b for a, b in zip(self.list, other.list))


Point.get_len = get_len
Point.__str__ = __str__

BrokenLine.__add__ = __add__


A = Point("A", 3, 4)
B = Point("B", 7, 9)

D = get_len(A, B)
print(D)
print(A.__str__(B))

# Экземпляры класса BrokenLine
br_1 = BrokenLine([Point("A", 3, 4), Point("B", 7, 9), Point("C", 1, 3)])
br_2 = BrokenLine([Point("E", 6, 8)])
br_3 = br_1 + br_2
print(br_3.list)

# -----------------------------------ДОПОЛНИТЕЛЬНО--------------------------------------
# 1) Ограничить сложение двух отрезков таким образом, чтобы
# складывались только те отрезки, которые имеют одну общую точку.
# Последовательность точек значения не имеет.
# 2) При сложении с экземпляром класса BrokenLine, точки отрезка
# должны добавиться в список точек ломанной.
# 3) При сложении с точкой должен вернуться объект BrokenLine.
