# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

def fctr(number):
    res = []
    d = 2
    while d * d <= number:
        if number % d == 0:
            res.append(d)
            number //= d
        else:
            d += 1
    if number > 1:
        res.append(number)
    return res


print(f'Простые множители введенного числа: {fctr(abs(int(input("Введите натуральное число: "))))}')
