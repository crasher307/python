# Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z (расшифровка этого выражения
# not (x[0] or x[1] or x[2] = not x[0] and not x[1] and not x[2]) для всех значений предикат.

check = [
    [0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 1],
    [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1],
]
result = []

for x in check:
    result.append(True if not (x[0] or x[1] or x[2]) == (not x[0] and not x[1] and not x[2]) else False)

result = 'ЛОЖЬЮ' if False in result else 'ИСТИНОЙ'
print(f'Утверждение "¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z" является {result}')
