# Создайте текстовый файл (шаблон), содержащий следующее:
# «Приветствую тебя, {{ user_name }}! Очень рад тебя видеть! С нашей
# последней встречи прошло {{ time }} лет… Прими этот {{ item }} и
# садись {{ place }}

# Ваша программа во время запуска должна запросить соответствующие данные у пользователя через консоль.
# Затем заполнить данный шаблон этими данными и вывести отрендеренный текст в консоль.

from jinja2 import Template

# {{ }} – выражение для вставки конструкций Python в шаблон;


class Person:
    def __init__(self, user_name, time, item, place):
        self.user_name = user_name
        self.time = time
        self.item = item
        self.place = place


per = Person(
    input("Введите user_name:"),
    int(input("Введите time(лет):")),
    input("Введите item:"),
    input("Введите place:"),
)


with open("jinja_one.txt", "w+", encoding="utf-8") as file:
    tm = Template(
        "«Приветствую тебя, {{ per.user_name }}! Очень рад тебя видеть!\nС нашей последней встречи прошло {{ per.time }} лет…\nПрими этот {{ per.item }} и садись {{ per.place }}."
    )
    msg = tm.render(per=per)
    file.write(msg)
    file.seek(0)
    print(file.read())
