mas = ["Москва", "Санкт-Петербург", "Лондон", "Париж", "Берлин"]
rez = 0

for i in range(len(mas)):
    rez += len(mas[i])
print(rez)


rez = 0
for i in mas:
    rez += len(i)
print(rez)


a = sum(len(i) for i in mas)
print(a)


rez2 = 0
for i in range(len(mas)):
    rez2 = (lambda x, y: x+len(mas[y]))(rez2, i)
print(rez2)
