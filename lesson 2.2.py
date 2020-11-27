def rep ():
    list[i], list[i + 1] = list[i + 1], list[i]
    print (list)
list = []
for i in range(int(input('Сколько значений будет в строке? '))):
    value = input('Введите эти значения: ')
    list.append(value)
if len(list) % 2 == 0:
    for i in range(0, (len(list)), 2):
        rep()
elif len(list) % 2 != 0:
    for i in range(0, (len(list)-1), 2):
       rep()