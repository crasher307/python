# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

from math import sqrt


class Point(object):
    x: None
    y: None

    def __init__(self, x, y):
        self.x = x
        self.y = y


def getCoord(message):
    xInp = 0
    yInp = 0
    while xInp == 0 or yInp == 0:
        xInp = int(input(f'{message} Введите координаты X: '))
        yInp = int(input(f'{message} Введите координаты Y: '))
        if xInp == 0 or yInp == 0:
            print('Попробуйте снова (X == 0 or Y == 0)')
    return Point(xInp, yInp)


def getDist(p1Inp, p2Inp):
    # AB = √((xb - xa)^2 + (yb - ya)^2)
    return sqrt(pow(p2Inp.x - p1Inp.x, 2) + pow(p2Inp.y - p1Inp.y, 2))


p1 = getCoord('1-ая точка')
p2 = getCoord('2-ая точка')
dist = round(getDist(p1, p2), 2)
print(f'Расстояние между точками ({p1.x}, {p1.y}) и ({p2.x}, {p2.y}) = {dist}')
