# Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.
# Пример:
# - 1, 4, 8, 7, 5 -> 8
# - 78, 55, 36, 90, 2 -> 90

from random import random

arr = []
for i in range(0, 5):
    # arr.append(int(input('Введите число: ')))
    arr.append(round(random() * 100))

print(f'Массив: {arr}\nМаксимальное число - {max(arr)}')
