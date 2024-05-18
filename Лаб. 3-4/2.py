# Создать класс Human. При создании экземпляра класса ему должны передаться в формате строки обязательные параметры: фамилия, имя, отчество.

# Также класс должен получить необязательные параметры возраст и пол.

# Возраст по умолчанию равен нулю. Пол указывается строкой «М» или «Ж», значение по умолчанию любое из 2х вариантов.

# В классе Human реализовать 2 метода:
# 1) get_fio – возвращает строку в формате «Фамилия И. О.»
# 2) get_full_info – возвращает строку в формате:

# Фамилия: {…}
# Имя: {…}
# Отчество: {…}
# Пол: {…}
# Возраст: {…}
# - где {…} соответствующее значение атрибута объекта. Переносы строк – обязательны.


# Наследование позволяет выделить общее для нескольких классов поведение и вынести его в отдельную сущность.
# То есть наследование является средством переиспользования кода (code reuse) — использования существующего кода для решения новых задач!

# Функция super () в Python позволяет наследовать базовые классы (они же суперклассы или родительские классы) без необходимости явно ссылаться на базовый класс.
# super позволяет вызывать повдение родительского класса

# Основное преимущество концепции наследования в программировании - это вынос одинакового кода из разных классов в один родительский класс


class Human:
    def __init__(self, name, surname, middlname, age=0, sex="«М» или «Ж»"):
        self.name = name
        self.surname = surname
        self.middlname = middlname
        self.age = age
        self.sex = sex

    def get_fio(self):
        return "{0} {1}.{2}.".format(self.surname, self.name[0], self.middlname[0])

    def get_full_info(self):
        return "Фамилия: {0}\nИмя: {1}\nОтчество: {2}\nПол: {3}\nВозраст: {4}".format(
            self.surname, self.name, self.middlname, self.sex, self.age
        )

        # return f"Фамилия: {self.surname}\nИмя: {self.name}\nОтчество: {self.middlname}\nВозраст: {self.age}\nПол: {self.sex}"


# Экземпляр класса
person = Human("Арина", "Крикунова", "Васильевна", 20, "Ж")

print("----------------------get_full_info()----------------------------------")
print(person.get_full_info())
print("----------------------get_fio()----------------------------------------")
print(person.get_fio())


print("----------------------class Student------------------------------------")

# Создать класс Student, который наследуется от класса Human.
# Переопределить в данном классе метод __init__ таким образом, чтобы он
# принимал обязательный параметр номера группы в формате строки.

# Переопределить метод get_full_info таким образом, чтобы к выводу добавилась строка «Группа: {…}».


class Student(Human):
    def __init__(self, name, surname, middlname, age, sex, ng):
        super().__init__(name, surname, middlname, age, sex)
        self.ng = ng

    def get_full_info(self):
        # вызываем метод родительского класса
        print(super().get_full_info())
        # Добавляем свое поведение
        return "Группа: {0}".format(self.ng)


p = Student(
    person.name, person.surname, person.middlname, person.age, person.sex, ng="ИСТБ-31"
)

print(p.get_full_info())


print("----------------------ДОПОЛНИТЕЛЬНО------------------------------------")

# Использование super – обязательно.
# Метод get_full_info для student должен предусматривать возможность возврата строки, где вместо переноса строк используется запятая.


class Student(Human):
    def __init__(self, name, surname, middlname, age, sex, ng):
        super().__init__(name, surname, middlname, age, sex)
        self.ng = ng

    def get_full_info(self):
        # вызываем метод родительского класса и добавляем свое поведение
        new_format = super().get_full_info().replace("\n", ",")
        return "{0},{1}".format(new_format, self.ng)
        # return f"{new_format},Группа: {self.ng}"


p = Student(
    person.name, person.surname, person.middlname, person.age, person.sex, ng="ИСТБ-31"
)

print(p.get_full_info())
