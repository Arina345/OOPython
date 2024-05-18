# Даны два файла (в Moodle) формата csv и json, содержащие разные списки городов, их население, регион и индекс.

# Данные из файлов необходимо соединить таким образом, чтобы они содержали только уникальные значения.

# Для этого создайте класс City, у которого будут реализованы методы __hash__ и __eq__.

# Поместите экземпляры класса в коллекцию, при правильно реализованных вышеуказанных методов коллекция будет содержать только уникальные города.

# Новый список городов необходимо сохранить в форматы CSV и JSON.
# Используйте собственные функции преобразований.

import csv, json

print(*[1, 1, 1, 1,1,1,1])
class City:
    def __init__(self, raw_data: dict):
        self.index = int(raw_data.get("Индекс"))
        self.tregion = raw_data.get("Тип региона")
        self.region = raw_data.get("Регион")
        self.city = raw_data.get("Город")
        self.pop = raw_data.get("Население")
        try:
            self.pop = int(self.pop)
        except:
            s = [i for i in self.pop if i.isdigit()]
            self.pop  = ''.join(s)
            self.pop = int(self.pop)
        
    def __str__(self) -> str:
        return f"name: {self.index}, tregion: {self.tregion}, region: {self.region}, city: {self.city}, population: {self.pop}"

    def __repr__(self) -> str:
        return f"City({self.index}): {self}"

    def __eq__(self, other):
        if isinstance(other, City):
            return self.index == other.index
        return False

    def __hash__(self) -> int:
        return hash(self.index)

    # ----------------------------------------ДОПОЛНИТЕЛЬНО--------------------------------------
    # Перед сохранением данных в файл отсортируйте список по численности населения.
    def __gt__(self, other):
        if isinstance(other, City):
            return self.pop > other.pop
        return False
    
    def as_dict(self):
        line = self.__dict__
        # print(line)
        result = {}
        result["Индекс"] = line.get("index")
        result["Тип региона"] = line.get("tregion")
        result["Регион"] = line.get("region")
        result["Город"] = line.get("city")
        result["Население"] = line.get("pop")
        return result


list1 = []

with open(
    "Города.csv",
    "r",
    newline="",
    encoding="utf-8",
) as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        list1.append(City(row))

# list_city = set(City(**p) for p in list1)

# Для чтения в модуле json есть два метода:

# json.load - метод считывает файл в формате JSON и возвращает объекты Python
# json.loads - метод считывает строку в формате JSON и возвращает объекты Python

# Чтение файла json
with open("города.json", "r", encoding="utf-8") as f:
    city = json.load(f)
# print(city)

for row in city['data']:
    c = City(row)
    list1.append(c)


list1 = set(list1)
list1 = list(list1)
list1.sort()
# --------------------------------------------ПРОВЕРКА-------------------------------------------------------


# for l in list_city[0:5]:
#     print(l.pop)


# for dicts in list1:
#     if dicts["pop"] == 963:
#         print(dicts)


# --------------------------------------------ЗАПИСЬ ФАЙЛА (CSV и JSON)-------------------------------------------------------

# writerow - записывает каждый список построчно;
# writerows - записывает список списков в файл целиком.


with open("City_newfile.csv", "w+", newline="", encoding="utf-8") as new_file:
    writer = csv.DictWriter(
        new_file,
        fieldnames=["Индекс", "Тип региона", "Регион", "Город", "Население"],
    )
    writer.writeheader()
    city: City
    for city in list1:
        writer.writerow(city.as_dict())


# Для записи информации в формате JSON в модуле json также два метода:

# json.dump - метод записывает объект Python в файл в формате JSON
# json.dumps - метод возвращает строку в формате JSON


# Параметр ensure_ascii в функции json.dumps() по умолчанию установлен в True. Это приводит к преобразованию не-ASCII символов в escape-последовательности.

# Если установить этот параметр в False, то функция json.dumps() будет сохранять все символы в исходном виде.

data = {"City": [item.as_dict() for item in list1]}


with open("City_newfile.json", "w", encoding="utf-8") as new_file:
    json.dump(data, new_file, indent=2, ensure_ascii=False)
    # new_file.write(json.dumps(data, indent=2, ensure_ascii=False))


# Хеши используются для быстрого сравнения ключей словаря во время поиска по нему.
# Хеш - это результат хеширования, т.е. операции по преобразованию данных в строку или число фиксированной длины.
