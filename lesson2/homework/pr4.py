# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в отдельном списке( пример n=4, lst1=[4,-2,1,3] - список на основе n, а позиции элементов lst2=[3,1].

import random

num = 4
arr = []
arr2 = [random.randint(0, num - 1), random.randint(0, num - 1)]
for i in range(num):
    arr.append(random.randint(-num, num))
print(f'{arr}\n{arr2}\narr[{arr2[0]}] * arr[{arr2[1]}] = {arr[arr2[0]]} * {arr[arr2[1]]} = {arr[arr2[0]] * arr[arr2[1]]}')
