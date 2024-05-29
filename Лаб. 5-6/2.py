# Определить метод приведения к строке (__str__) таким образом, чтобы возвращалась строка следующего формата:

# {Имя точки}({координата x},{координата y}) , пример А(3,4)

# Определить метод сравнения (__eq__) и уникальности (__hash__) для точки.

# Продемонстрировать работу методов путем сравнения двух экземпляров и создания коллекции (set) экземпляров длинною не менее 5 шт.

# Добавить метод сложения (__add__).
# При сложении двух точек должен возвращаться новый экземпляр класса Segment.


from one import Segment, BrokenLine


class Point:
    def __init__(self, name, x, y):
        self.n = name
        # -----------------------------------ДОПОЛНИТЕЛЬНО--------------------------------------
        # 3) Скрыть от пользователя прямой доступ к атрибутам координат точек.
        self.__x = x
        self.__y = y

    # -----------------------------------ДОПОЛНИТЕЛЬНО--------------------------------------
    # Изменение координат реализовать через метод set_coordinate.
    def set_coordinate(self, coordinate, value):
        match coordinate:
            case "x":
                self.__x = value
            case "y":
                self.__y = value

    # -----------------------------------ДОПОЛНИТЕЛЬНО--------------------------------------
    # Получение текущей координаты реализовать через метод get_coordinate
    def get_coordinate(self, coordinate):
        match coordinate:
            case "x":
                return self.__x
            case "y":
                return self.__y

    def __str__(self) -> str:
        return f"{self.n}({self.__x},{self.__y})"

    def __repr__(self) -> str:
        return f"{self.n}({self.__x},{self.__y})"

    def __eq__(self, other):
        return self.n == other.n and self.__x == other.__x and self.__y == other.__y

    def __hash__(self) -> int:
        return hash((self.__x, self.__y, self.n))

    def __add__(self, other):
        if isinstance(self, Point):
            if isinstance(other, Point):
                return Segment(self, other)
            elif isinstance(other, Segment):
                return BrokenLine([self, other, Point("H", 5, 5), Point("R", 3, 2)])
            elif isinstance(other, BrokenLine):
                other.points.append(self)
                return BrokenLine(other.points)
            return BrokenLine(self.points + other.points)


# Экземпляры класса
A = Point("A", 3, 4)
B = Point("B", 6, 8)
C = Point("C", 6, 5)

print(
    "--------------------------------------ПРОВЕРКА-------------------------------------------"
)
print(A == C)
collection = set([A, A, B, C, C])
print(collection)


print("Сложение двух точек и возвращение экземпляра класса Segment", A.n + B.n)
print(
    "При сложении с классом Segment должен возвращаться экземпляр класса BrokenLine",
    A + Segment(B, C),
)


br = Point("D", 8, 12) + BrokenLine([A, B, C])

print(
    "При сложении с классом BrokenLine, последний должен расширить свой список точек",
    br.points,
)
print()

# Изменение координаты
A.set_coordinate("x", 6)
print(f"Получение значения координаты x:", A.get_coordinate("x"))
