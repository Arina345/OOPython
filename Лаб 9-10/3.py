# В прошлой работе Вы получили список городов в формате json или csv.
# Необходимо сделать шаблон в формате html. Шаблон необходимо заполнить
# данными из Ваших файлов и сохранить как result.html.
# «добавление стилей в самом html документе или подключение файла css
# для более приятного отображения – приветствуется»


# -----------------------------------ДОПОЛНИТЕЛЬНО--------------------------------------
# Ваша программа должна перед рендерингом запросить наименьшее
# количество население города для помещения его в шаблон. То есть города, чье
# население ниже установленной планки не должны присутствовать в
# result.html. Фильтрация должна быть заложена в шаблон.

from jinja2 import Template
import json


minpop = int(input("Введите наименьшее количество населения города:"))

with open("Города.json", "r", encoding="utf-8") as f:
    city = json.load(f)
for section, commands in city.items():
    for c in commands:
        if type(c["Население"]) == str:
            s = [i for i in c["Население"] if i.isdigit() != True]
            for el in s:
                c["Население"] = c["Население"].replace(el, "")
            c["Население"] = int(c["Население"])

html_template = """<html>
<head>
<title> Задание 3.Лабораторная работа 9-10 </title>
<link rel="stylesheet"  href="css/style.css">
<script src="filter.js"></script>
</head>
<body>
<div class = "main-header">
    <img class="logo" src = "css/img/icon.png" wigth = 50px height=50px>
    <p>arinakrikunova.com</p></div>
<div class="container">
<div class="city-info">
<table id="city-select">
<thead>
<th col-index=1>Индекс</th> 
<th col-index=2>Тип региона
<select class="table-filter" onchange="filter_rows()">
        <option value="all">Показать все</option>
    </select>
</th>
<th col-index=3>Регион
    <select class="table-filter" onchange="filter_rows()">
        <option value="all">Показать все</option>
    </select>
</th>
<th col-index=4>Город
    <select class="table-filter" onchange="filter_rows()">
        <option value="all">Показать все</option>
    </select>
</th>
<th col-index=5>Население</th>
</thead> 
<tbody class="info"> 
<tr>
{% set sorted_data = commands|sort(attribute="Население") %}
{% for i in range(sorted_data|length)%}
{% set n = minpop %}
{% if sorted_data[i]["Население"]|int > n %}
<td class="index"><div class = "circle">{{sorted_data[i]["Индекс"]}}</div></td>
<td class="tregion">{{sorted_data[i]["Тип региона"]|title}}</td>
<td>{{sorted_data[i]["Регион"]}}</td>
<td>{{sorted_data[i]["Город"]}}</td>
<td class = "pop">
{{sorted_data[i]["Население"]}}
<div class="circlepop"></div></td>
</tr>
</tbody>
{% endif %}
{% endfor%}
</div>
</div>
</table>
<script>
window.onload = () => {
console.log(document.querySelector("#city-select > tbody > tr:nth-child(1) > td:nth-child(2) ").innerHTML);};
getUniqueValuesFromColumn()
</script>
</body></html>
"""
tm = Template(html_template)
msg = tm.render(commands=commands, minpop=minpop)

with open("website/result.html", "w+", encoding="utf-8") as html:
    html.write(msg)

# Присвоение переменных в шаблонах jinja2 _ {% set name_variable = value%}
