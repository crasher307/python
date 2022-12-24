# Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# (если получаются длинные числа после запятой, это нормально и особенность данного языка программирования.
# ваш ответ может не совпадать с примером (может получиться 0,20))
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random


def minMax(A):
    num = round(A[0] % 1, 2)
    aMin = num
    aMax = num
    for item in A:
        num = round(item % 1, 2)
        if num < aMin:
            aMin = num
        if num > aMax:
            aMax = num
    return [aMin, aMax]


arr = []
for i in range(random.randint(4, 10)):
    arr.append(round(random.randint(0, 9) + random.random(), 2))

[minA, maxA] = minMax(arr)
res = round(maxA - minA, 2)

print(f'Data: {arr}\nMin: {minA}, Max: {maxA}\nResult: {res}')
