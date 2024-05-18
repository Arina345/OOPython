# Создать классы Cat, Dog и Chicken.
# Для каждого класса создать метод get_sound и атрибут name.

# При обращении к атрибуту name должна возвращаться строка, содержащая кличку питомца

# При вызове метода get_sound в зависимости от класса в консоль должен
# выводиться следующий текст:

# «мяю» - для Cat,
# «гав-гав» - для Dog,
# «чик-чик» - для Chicken.

# Создайте список Animals, содержащий не менее 3х экземпляров каждого класса.
# Затем создайте цикл, в котором у каждого элемента списка будет выведен на экран атрибут name и вызван метод get_sound.

# Для каждого класса создать метод add_friend, при вызове данного метода, ему должен аргументом передаться любой объект.
# Переданный объект должен расширить список «друзей» экземпляра класса, являющимся атрибутом friends.


# ДОПОЛНИТЕЛЬНО

# В методе add_friend должна осуществляться проверка добавляемого объекта.

# Каждый класс может иметь в «друзьях» не более 2х типов объектов и не более пяти экземпляров в общей сумме.
# То есть, для класса должны быть определены два типа объектов, которых можно добавить в список, и суммарно в этом списке может быть не более пяти элементов.

# Реализовать метод «список друзей» для каждого класса: на экран выводится имя каждого элемента списка или сообщение о пустоте списка.


class Cat:
    def __init__(self, name):
        self.name = name
        self.friend = []

    def get_sound(self):
        return "мяу"

    def add_friend(self, friends):
        if isinstance(friends, (Dog, Chicken, str)) == True:
            self.friend.append(friends)
        else:
            raise ValueError("Объект такого типа нельзя добавить")
        if len(self.friend) > 5:
            raise ValueError("В списке больше 5 элементов")

    def list_friend(self):
        if len(self.friend) > 0:
            for f in self.friend:
                print(f)
        else:
            print([])


class Dog:
    def __init__(self, name):
        self.name = name
        self.friend = []

    def get_sound(self):
        return "гав-гав"

    def add_friend(self, friends):
        if isinstance(friends, (Cat, Chicken, str)) == True:
            self.friend.append(friends)
        else:
            raise ValueError("Объект такого типа нельзя добавить")
        if len(self.friend) > 5:
            raise ValueError("В списке больше 5 элементов")

    def list_friend(self):
        if len(self.friend) > 0:
            for f in self.friend:
                print(f)
        else:
            print([])


class Chicken:
    def __init__(self, name):
        self.name = name
        self.friend = []

    def get_sound(self):
        return "чик-чик"

    def add_friend(self, friends):
        if isinstance(friends, (Cat, Dog, str)) == True:
            self.friend.append(friends)
        else:
            raise ValueError("Объект такого типа нельзя добавить")
        if len(self.friend) > 5:
            raise ValueError("В списке больше 5 элементов")

    def list_friend(self):
        if len(self.friend) > 0:
            for f in self.friend:
                print(f)
        else:
            print([])


# Экземпляры классов Cat, Dog, Chicken
cat = Cat("Персик")
dog = Dog("Сеня")
chicken = Chicken("Федор")

print(cat.name, cat.get_sound(), sep="\t")

print(dog.name, dog.get_sound(), sep="\t")

print(chicken.name, chicken.get_sound(), sep="\t")

print("--------------------------------------------------------")

# --------------------------------------------------------------------------------------------------------------------------------

animals_names = [
    "Барсик",
    "Рей",
    "Федор",
    "Вася",
    "Арчи",
    "Петя",
    "Кеша",
    "Коля",
    "Женя",
]

animals = [(Cat, Dog, Chicken)[i % 3](animals_names[i]) for i in range(9)]


for animal in animals:
    print(
        "Кличка:{}".format(animal.name), "Звук:{}".format(animal.get_sound()), sep="\t"
    )
    print()


# --------------------------------------------------------------------------------------------------------------------------------
print("----------------------ДОПОЛНИТЕЛЬНО----------------------------------")


# Добавление друзей


# ---------------------------------------------------ДРУЗЬЯ CATE-----------------------------------------------------------------------------
print("----------------------ДРУЗЬЯ CATE----------------------------------")

cat_friend = [
    Cat("Степан").name,
    Dog("Пупс"),
    Dog("Пупс"),
    Chicken("Петя"),
    Cat("Мина").name,
]

for f in cat_friend:
    cat.add_friend(f)

cat.list_friend()


# ---------------------------------------------------ДРУЗЬЯ DOG-----------------------------------------------------------------------------
print("----------------------ДРУЗЬЯ DOG----------------------------------")

dog_friend = [
    Dog("Степан").name,
    Cat("Пупс"),
    Chicken("Петя"),
    Cat("Мина").name,
]

for d in dog_friend:
    dog.add_friend(d)

dog.list_friend()


# ---------------------------------------------------ДРУЗЬЯ CHICKEN-----------------------------------------------------------------------------
print("----------------------ДРУЗЬЯ CHICKEN----------------------------------")

chicken_friend = [Dog("Степан"), Cat("Пупс"), Chicken("Петя").name]

for c in chicken_friend:
    chicken.add_friend(c)

chicken.list_friend()
