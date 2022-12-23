# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

num = float(input('Введите вещественное число: '))
string = str(num)
s = 0
for ch in string:
    try:
        s += int(ch)
    except ValueError:
        pass
    except Exception as error:
        print(f'Error: {error}')
print(f'Сумма цифр числа {num} = {s}')
