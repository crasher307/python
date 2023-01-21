# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

import random

arr = []
for i in range(random.randint(5, 20)):
    arr.append(random.randint(0, 9))

# s = 0
# for i in range(1, len(arr), 2):
#     s += arr[i]
#
# print(f'Data: {arr}\nResult: {s}')

print(f'Data: {arr}\nResult: {sum(arr[1::2])}')
