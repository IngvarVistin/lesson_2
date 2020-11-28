rating = [7, 5, 3, 3, 2]
n = 0
number = int(input('Введите число: '))
while number < rating[n]:
    n = n+1
else: rating.insert(n, number)
print(rating)