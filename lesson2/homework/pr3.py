# Задайте список из n чисел последовательности (1+1/n)**n и выведите на экран их сумму.

num = int(input('Введите число: '))
arr = []
for i in range(1, num + 1):
    arr.append(round((1 + 1 / i) ** i, 2))
print(f'(1 + 1 / n) ** n: {arr}\nСумма: {round(sum(arr), 2)}')
