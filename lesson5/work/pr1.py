# Расчитать нод двух чисел(быстрый и медленный способ)
from math import gcd


def NOD(a1, a2):
    return gcd(a1, a2)
    # if a1 < a2:
    #     a1, a2 = a2, a1
    # if a2 == 0:
    #     return a1
    # else:
    #     return NOD(a2, a1 % a2)


num1 = 28
num2 = 8
print(f'num1: {num1}, num2: {num2}, НОД: {NOD(num1, num2)}')