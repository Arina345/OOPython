# Программа должна запросить у пользователя следующую информацию:
# 1) имена двух персонажей;
# 2) вид соревнования;
# 3) характеристики персонажей в данном виде деятельности.

# Подготовьте шаблон, в который при рендеринге передастся полученная
# информация. В результате рендеринга должен быть получен текст,
# содержащий имя победителя (побеждает тот, чьи характеристики больше).

# При равенстве вывести соответствующею информацию. Сравнение
# характеристик должно происходить в блоке if шаблонизатора.

from jinja2 import Template
import json
import datetime


class Sportsman:
    def __init__(self, spname_one, spname_two, tpsport, chperone, chpertwo):
        self.spname_one = spname_one
        self.spname_two = spname_two
        self.tpsport = tpsport
        self.chperone = chperone
        self.chpertwo = chpertwo


sp = Sportsman(
    # input("Введите имя первого персонажа:"),
    # input("Введите имя второго персонажа:"),
    # input("Введите вид спорта:"),
    # input("Введите характеристику первого персонажа:"),
    # input("Введите характеристику второго персонажа:"),
    "Андрей",
    "Федор",
    "Хоккейный матч",
    " +3Кп, 10 голевых",
    " +3Кп, 9 голевых",
)


about = """Имя первого персонажа: {{sp.spname_one}}
Имя второго персонажа: {{sp.spname_two}}
Вид соревнования: {{sp.tpsport}}
Характеристика первого персонажа:{{sp.chperone}}
Характеристика второго персонажа:{{sp.chpertwo}}
Победитель:{% if sp.chperone|length>sp.chpertwo|length%}{{sp.spname_one}}
{% elif sp.chperone|length<sp.chpertwo|length%}{{sp.spname_two}}{% else %}{{n}}{% endif %}
"""
tm_one = Template(about)
msg_one = tm_one.render(sp=sp, n="НИЧЬЯ")
# print(msg_one)


# -----------------------------------ДОПОЛНИТЕЛЬНО--------------------------------------
# Вывод на экран должен быть в формате json или csv. Оба формата
# должны содержать следующие поля:
# 1) имя победителя
# 2) его характеристики
# 3) вид соревнования
# 4) дата проведения соревнования
# Имена полей произвольные.


winner = """Имя победителя: 
{% if sp.chperone|length>sp.chpertwo|length%}
    {{sp.spname_one}}.
    Характеристика победителя:{{sp.chperone}}.
    Вид соревнования:{{sp.tpsport}}.
    Дата проведения: {{date.strftime("%d/%m/%y")}}.
{% elif sp.chperone|length<sp.chpertwo|length%}
    {{sp.spname_two}}.
    Характеристика победителя:{{sp.chpertwo}}.
    Вид соревнования:{{sp.tpsport}}.
    Дата проведения: {{date.strftime("%d/%m/%y")}}.
{% elif sp.chperone|length==sp.chpertwo|length %}
    Имя победителя:{{n}}.Вид соревнования:{{sp.tpsport}}.Дата проведения:{{date.strftime("%d/%m/%y")}}
{% endif %}"""

tm_two = Template(winner)
msg_two = tm_two.render(sp=sp, n=msg_one, date=datetime.datetime.today())
print(msg_two)


with open("jinja_two.json", "w+", encoding="utf-8") as json_file:
    json_file.write(json.dumps(msg_two, ensure_ascii=False))
    json_file.seek(0)
    print(json_file.read())
