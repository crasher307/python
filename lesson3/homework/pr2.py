# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

import random

arr = []
for i in range(random.randint(4, 20)):
    arr.append(random.randint(0, 9))

res = []
half = (len(arr) / 2).__floor__()

for i in range(half):
    res.append(arr[i] * arr[len(arr) - 1 - i])

if len(arr) % 2 != 0:
    res.append(arr[half] ** 2)

print(f'Data: {arr}\nResult: {res}')
