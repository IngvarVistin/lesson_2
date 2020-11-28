line = input('Введите строку из нескольких слов, разделённых пробелами ')
list = line.split()
for number, list in enumerate(list, 1):
    print(number, list[0:10])
