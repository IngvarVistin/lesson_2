months = int(input('Введите цифру месяца от 1 до 12: '))
dict_months = {
    1: 'January',
    2: 'February',
    3: 'March',
    4: 'April',
    5: 'May',
    6: 'Junio',
    7: 'Julio',
    8: 'Agosto',
    9: 'Septiembre',
    10: 'Octubre',
    11: 'November',
    12: 'December'
}
print(dict_months[months])
season = ['Winter', 'Spring', 'Summer', 'Autumn']
if months == 1 or months == 2 or months == 12:
    print(season[0])
elif months == 3 or months == 4 or months == 5:
    print(season[1])
elif months == 6 or months == 7 or months == 8:
    print(season[2])
elif months == 9 or months == 10 or months == 11:
    print(season[3])
