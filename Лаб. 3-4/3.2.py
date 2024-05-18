print(
    "----------------------ДОПОЛНИТЕЛЬНО(ПРОДОЛЖЕНИЕ)------------------------------------"
)


# Создать еще один класс NewTriangle.
class NewTriangle:
    protected_attrs = ("__one", "__two", "__three")

    def __init__(self, one, two, three):
        self.__one = one
        self.__two = two
        self.__three = three
        self.replace_attr()

    # Но изменять эти атрибуты должно быть возможно только внутри класса предназначенными для этого методами.
    def __setattr__(self, key, value):
        if key in self.protected_attrs:
            raise AttributeError(f"Нельзя установить данный атрибут {key}")
        super().__setattr__(key, value)

    def replace_attr(self):
        self.__one = 5
        self.__two = 7
        self.__three = 11


tr = NewTriangle(6, 7, 2)

try:
    tr.__one = 5
    tr.__two = 7
    tr.__three = 11
except:
    print("Не удается изменить значения")

# Добиться возможности смотреть длину стороны вне класса, обращаясь к его атрибутам.
print(tr._NewTriangle__one, tr._NewTriangle__two, tr._NewTriangle__three, sep="\n")
