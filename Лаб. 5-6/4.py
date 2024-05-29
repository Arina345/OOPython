from math import sqrt
from one import BrokenLine, Point, Segment


# Определить метод get_len для вычисления длины ломанной линии.
# По сути необходимо попарно перебрать точки, образуя отрезки.
# Длина ломанной будет ровна сумме длин отрезков.
def get_len(self):
    length = 0
    for i in range(len(self.points) - 1):
        if isinstance(self.points[i], Point):
            x1, y1 = self.points[i].x, self.points[i].y
            if isinstance(self.points[i + 1], Point):
                x2, y2 = self.points[i + 1].x, self.points[i + 1].y
            else:
                x2, y2 = self.points[i + 1].p2.x, self.points[i + 1].p2.y
        elif isinstance(self.points[i], Segment):
            x1, y1 = self.points[i].p1.x, self.points[i].p1.y
            if isinstance(self.points[i + 1], Segment):
                x2, y2 = self.points[i + 1].p2.x, self.points[i + 1].p2.y
            else:
                x2, y2 = self.points[i + 1].x, self.points[i + 1].y
        segment_length = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
        length += segment_length
    return f"Длина ломанной будет равна сумме длин отрезков {length}"


# Определить метод __str__ таким образом, чтобы итоговая строка
# содержала перечисление имен точек через запятую. Пример: A,B,C


def __str__(self) -> str:
    result = []
    for point in self.points:
        if isinstance(point, Point):
            result.append(point.n)
        elif isinstance(point, Segment):
            result.append(f"{point.p1.n}{point.p2.n}")
    return ",".join(result)


# -----------------------------------ДОПОЛНИТЕЛЬНО--------------------------------------
# 1) При создании экземпляра две последовательные точки не должны быть одинаковыми.
# 2) Определить метод сложения с остальными классами из данной
# работы. Экземпляр ломанной линии должен расширять список своих
# точек за счет точек объектов с которыми он складывается.
def __add__(self, other):
    if isinstance(other, (Point, Segment)):
        if isinstance(other, Point):
            if self.points[-1].n != other.n:
                self.points.append(other)
            return BrokenLine(self.points)
        elif isinstance(other, Segment) and isinstance(self.points[-1], Point):
            if self.points[-1].n != other.p1.n + other.p2.n:
                self.points.append(other)
            return BrokenLine(self.points)
        elif isinstance(other, Segment) and not isinstance(self.points[-1], Point):
            if (self.points[-1].p1.n + self.points[-1].p2.n) != (
                other.p1.n + other.p2.n
            ):
                self.points.append(other)
            return BrokenLine(self.points)
    return BrokenLine(self.points + other.points)


BrokenLine.get_len = get_len
BrokenLine.__str__ = __str__
BrokenLine.__add__ = __add__


A = Point("A", 3, 4)
B = Point("B", 6, 8)
C = Point("C", 4, 9)
D = Point("D", 2, 7)

l = (
    BrokenLine([A, B, C, D])
    + Point("F", 2, 2)
    + Point("F", 2, 2)
    + Point("E", 5, 2)
    + Point("C", 5, 2)
    + Segment(A, D)
)
print(f"{l}\n{l.get_len()}")
