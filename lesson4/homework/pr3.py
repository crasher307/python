# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

import random

arr = []
for i in range(50):
    arr.append(random.randint(0, 50))

print(f'{arr}\n{list(set(arr))}')
