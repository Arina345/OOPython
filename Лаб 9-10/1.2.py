# -----------------------------------ДОПОЛНИТЕЛЬНО--------------------------------------

# Подготовьте файл ответов в формате json. При наличии этого файла программа не будет запрашивать у пользователя данные,
# а должная считать их из этого файла.

import json
from jinja2 import Template
import random
data = {
    "data": [
        {"user_name": "Арина", "time": 5, "item": "подарок", "place": "сюда"},
        {
            "user_name": "Анна",
            "time": 7,
            "item": "момент вечности",
            "place": "на лавку",
        },
        {
            "user_name": "Дана",
            "time": 9,
            "item": "букет",
            "place": "на кресло",
        },
    ]
}

with open("jinja_one.json", "w+", encoding="utf-8") as json_file:
    json.dump(data, json_file, indent=2, ensure_ascii=False)

with open("jinja_one.json", "r", encoding="utf-8") as json_file:
    person = json.load(json_file)
    for section, command in person.items():
        command = random.choice(command)
        print(command)


tm = Template(
    "«Приветствую тебя, {{c.user_name}}! Очень рад тебя видеть!\nС нашей последней встречи прошло {{c.time}} лет…\nПрими этот {{c.item }} и садись {{c.place}}."
)
msg = tm.render(c=command)
print(msg)
