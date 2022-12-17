# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка.
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

def getCoord():
    xInp = 0
    yInp = 0
    while xInp == 0 or yInp == 0:
        xInp = int(input('Введите координаты X: '))
        yInp = int(input('Введите координаты Y: '))
        if xInp == 0 or yInp == 0:
            print('Попробуйте снова (X == 0 or Y == 0)')
    return xInp, yInp


def getQtr(xInp, yInp):
    if xInp == 0 & yInp == 0:
        return 0
    switch = {
        'True True': 1,
        'False True': 2,
        'False False': 3,
        'True False': 4
    }
    return switch[f'{xInp > 0} {yInp > 0}']


(x, y) = getCoord()
qtr = getQtr(x, y)
print(f'Точка с координатами ({x}, {y}) находится в {qtr} четверти')
