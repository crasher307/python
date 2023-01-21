# Расчитать нод двух чисел(быстрый и медленный способ)
from math import gcd


# def NOD(a1, a2):
#     if a2 == 0:
#         return a1
#     else:
#         return NOD(a2, a1 % a2)


num1 = 28
num2 = 8

# print(f'num1: {num1}, num2: {num2}, НОД: {NOD(num1, num2)}')
print(f'num1: {num1}, num2: {num2}, НОД: {gcd(num1, num2)}')



# a=20
# b=58
#
# if a < b :
#     a, b = b, a
#
# while b!=0:
#     a, b = b, a % b
#
# print(a)
#
# _____________________________
#
# a=20
# b=75
#
# while a != b:
#     if a > b:
#         a -= b
#     else:
#         b -= a
#
# print(a)
