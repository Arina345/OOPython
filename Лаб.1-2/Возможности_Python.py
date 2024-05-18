l = ["12", 3, 5432, "2312"]

for index, i in enumerate(l, 1):
    print(index, "-", i)


for i in range(len(l)):
    element = l[i]
    print(i + 1, "-", element)
