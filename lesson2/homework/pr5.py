# Реализуйте алгоритм перемешивания списка. (рандомно поменять местами элементы списка между собой)

import random

arr = []
arr2 = []
count = 10

for i in range(count):
    arr.append(random.randint(0, 9))
arr2 = arr.copy()

point = None
for i in range(len(arr2)):
    point = random.randint(0, count - 1)
    (arr2[i], arr2[point]) = (arr2[point], arr2[i])

print(f'Start: {arr}\nEnd:   {arr2}')
