# Вычислить число c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

import math

print(round(math.pi, int(input('Введите кол-во знаков после запятой: '))))

# num = 0
# pi = math.pi
# while not (10 ** -10 <= num <= 10 ** -1):
#     try:
#         num = float(input('Введите число (прим.: 0.001): '))
#     except ValueError:
#         print('Требуется ввести дробное число')
# print(float(str(pi)[0:len(str(num)):]))
