rating = [7, 5, 3, 3, 2]
for i in range(int(input('Сколько чисел будете вводить?  '))):
    n = 0
    number = int(input('Введите число: '))
    while number < rating[n]:
        if n < len(rating)-1:
            n = n+1
        elif n >= len(rating)-1:
            rating.insert(n+1, number)
            break
    else: rating.insert(n, number)
    print(rating)