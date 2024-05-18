# доступные методы
# print(dir(c))

# Создайте класс Triangle (треугольник).
# Атрибуты, хранящие величину длины сторон треугольника, не должны быть доступны для чтения вне класса.

# При создании экземпляра класса в метод __init__ должны передаваться
# величины, соответствующие длинам сторон треугольника.

# Проверку устанавливаемых величин в данном методе делать не обязательно.


class Triangle:

    def __init__(self, lengthone, lengthtwo, lengthtree):
        self.__one = lengthone
        self.__two = lengthtwo
        self.__three = lengthtree
        self.triangle_rule()

    # Создайте отдельный метод на изменение каждого скрытого атрибута с
    # проверкой присваемого значения на соответствие правилу треугольника:
    # длина одной стороны не должна превышать сумму длин остальных сторон.
    def set_length(self, side_name, value):
        match side_name:
            case 'one':
                self.__one = value
            case 'two':
                self.__two = value
            case 'three':
                self.__three = value
        self.triangle_rule()
    
    def get__length(self, side_name):
        match side_name:
            case 'one':
                return self.__one 
            case 'two':
                return self.__two 
            case 'three':
                return self.__three
    

    def triangle_rule(self):
        if self.__one > self.__two + self.__three:
            raise AttributeError(
                f"Не выполянется правило треуголника. Измените первое значение {self.__one}!"
            )
        if self.__two > self.__one + self.__three:
            raise AttributeError(
                f"Не выполянется правило треуголника. Измените второе значение {self.__two}!"
            )
        if self.__three > self.__one + self.__two:
            raise AttributeError(
                f"Не выполянется правило треуголника. Измените третье значение {self.__three}!"
            )

    # Создайте метод get_perimetr, который возвращает длину периметра.
    def get_perimetr(self):
        self.triangle_rule()
        return self.__one + self.__three + self.__two

    # ----------------------ДОПОЛНИТЕЛЬНО------------------------------------

    # Для запрета смены величины атрибута длины стороны используйте метод __setattr__.
    # Новую величину в соответствующем методе необходимо задавать так: super().__setattr__(key, value).
    # Пример будет доступен в дополнительных материалах к курсу.

    def __setattr__(self, key, value):
        # if key in self.protected_attrs:
        if key == "__one":
            raise AttributeError(f"Нельзя установить данный атрибут {key}")

        super().__setattr__(key, value)


# Экземпляр класса
c = Triangle(16, 14, 24)
# c.set_length('one', 1)
print(c.get__length('one'))
# c._Triangle__one = 6
# print(c.__dict__)
# c._Triangle__one = 6
print(c.get_perimetr())
