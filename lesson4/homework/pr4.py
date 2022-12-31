# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random

k = abs(int(input('Введите нат. степень: ')))
kf = [random.randint(0, 100) for i in range(k + 1)]
poly = []
for i in range(len(kf) - 1, -1, -1):
    if kf[i] == 0:
        continue
    poly.append(f'{kf[i]}{"x" if i > 0 else ""}{f"^{i}" if i > 1 else ""}')
poly = f'{" + ".join(poly)} = 0'
print(poly)

f = open('pr4.log', 'a+')
f.write(f'{poly}\n')
f.close()
