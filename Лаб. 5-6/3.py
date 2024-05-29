from one import Point, BrokenLine, Segment
from math import sqrt


# Определить метод get_len для вычисления длины отрезка. Длина отрезка
# вычисляется следующим образом: (формула)
def get_len(self):
    L = sqrt((self.p1.x - self.p2.x) ** 2 + (self.p1.y - self.p2.y) ** 2)
    return L


# Определить метод приведения к строке. Пример: AB(xa, ya; xb, yb)
def __str__(self):
    return f"{self.p1.n}{self.p2.n} ({self.p1.x}a, {self.p1.y}a; {self.p2.x}b, {self.p2.y}b)"


# Определить метод сложения двух отрезков таким образом, чтобы возвращался новый экземпляр класса BrokenLine.


# -----------------------------------ДОПОЛНИТЕЛЬНО--------------------------------------
# 1) Ограничить сложение двух отрезков таким образом, чтобы
# складывались только те отрезки, которые имеют одну общую точку. Последовательность точек значения не имеет.
def __add__(self, other):
    if isinstance(self, Segment) and isinstance(other, Segment):
        if self.p2.n == other.p1.n:
            return BrokenLine([self.p1.n + other.p2.n, A, B])
        elif self.p1.n == other.p2.n:
            return BrokenLine([self.p2.n + other.p1.n, A, B])
        elif self.p1.n == other.p1.n:
            return BrokenLine([self.p2.n + other.p2.n, A, B])
        elif self.p2.n == other.p2.n:
            return BrokenLine([self.p1.n + other.p1.n, A, B])
        return "Отрезки не имеют общей точки"
    # -----------------------------------ДОПОЛНИТЕЛЬНО--------------------------------------
    # 2) При сложении с экземпляром класса BrokenLine, точки отрезка должны добавиться в список точек ломанной.
    elif isinstance(self, Segment) and isinstance(other, BrokenLine):
        # new_points = other.points + [self.p1.n, self.p2.n]
        return BrokenLine(other.points + [self.p1.n, self.p2.n])
    # -----------------------------------ДОПОЛНИТЕЛЬНО--------------------------------------
    # 3) При сложении с точкой должен вернуться объект BrokenLine
    elif isinstance(self, Segment) and isinstance(other, Point):
        return BrokenLine(
            [
                self.p1.n + self.p2.n + other.n,
                self.p1.x + self.p2.x + other.x,
                self.p1.y + self.p2.y + other.y,
            ]
        )


def __repr__(self):
    return f"{self.p1.n}{self.p2.n} ({self.p1.x}a, {self.p1.y}a; {self.p2.x}b, {self.p2.y}b)"


Segment.get_len = get_len
Segment.__str__ = __str__
Segment.__add__ = __add__
Segment.__repr__ = __repr__


def __repr__(self):
    return f"{self.points}"


BrokenLine.__repr__ = __repr__


A = Point("A", 3, 4)
B = Point("B", 6, 8)
C = Point("C", 4, 9)
D = Point("D", 2, 7)


print(
    "----------------------------Длина отрезка----------------------------------------------------"
)
l = Segment(A, B)
print(l.get_len())


print(
    "----------------------------Сложение двух отрезков-------------------------------------------"
)

segment1 = Segment(A, C)
segment2 = Segment(C, B)

total_len = segment1 + segment2
print(total_len)
print()
print(
    "2) При сложении с экземпляром класса BrokenLine, точки отрезка должны добавиться в список точек ломанной:",
    Segment(A, C)
    + BrokenLine([D.n, Point("K", 2, 1).n, Point("C", 2, 0).n, Point("B", 2, 2).n]),
)

print("3) При сложении с точкой должен вернуться объект BrokenLine:", Segment(A, C) + D)
