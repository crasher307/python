# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется
# жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний
# ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота "интеллектом"
import random


class Candy:
    __allCandy = 2021
    __minCandy = 1
    __maxCandy = 28

    def __call__(self, count=None):
        if count is not None:
            if not (self.__minCandy <= count <= self.__maxCandy):
                return False
            self.__allCandy -= count
        return self.__allCandy

    def min(self):
        return self.__minCandy if self.__minCandy <= self.__allCandy else self.__allCandy

    def max(self):
        return self.__maxCandy if self.__maxCandy <= self.__allCandy else self.__allCandy

    def baseMax(self):
        return self.__maxCandy


class Player(object):
    __descObject = None
    __countCandy = 0
    lastCount = 0
    isBot = True
    isWin = False
    playerName = None

    def __init__(self, descObject, name='Bot'):
        self.__descObject = descObject
        self.playerName = name
        self.isBot = False if 'Bot' not in name else True

    def __call__(self, count=None):
        if count is not None:
            if self.__descObject(count) is False:
                print(f'Некорректное значение, введите от {self.__descObject.min()} до {self.__descObject.max()}')
                return False
            self.lastCount = count
            self.__countCandy += count
            if self.__descObject.max() == 0:
                self.isWin = True
        return self.__countCandy


def readInput(func, message):
    try:
        return func(input(message))
    except ValueError:
        return False


def botSet(descObject):
    # return random.randint(descObject.min(), descObject.max())
    if descObject() > descObject.max() * 2:
        res = descObject.max()
    elif descObject() > descObject.max() + descObject.min():
        res = descObject() - descObject.max() - descObject.min()
    else:
        res = descObject.max()
    return res


desc = Candy()
players = [
    Player(desc, input('Введите имя: ')),
    Player(desc, 'Bot_1')
]
while desc() > 0:
    for pl in players:
        if desc() == 0:
            continue
        nextPlayer = False
        while nextPlayer is False:
            msg = f'На столе {desc()} конфет, сколько берем [{desc.min()}..{desc.max()}]: '
            cnt = botSet(desc) if pl.isBot else readInput(int, msg)
            nextPlayer = pl(cnt) is not False
            if not nextPlayer:
                break
    print(f'Конфет у игроков:')
    # [print(f'\t{pl()}\t: (+{pl.lastCount})\t{pl.playerName}' + (f' ♛ победитель ♛' if pl.isWin else '')) for pl in players]
    [print(f'\t{pl.playerName}\t{pl()}' + (f' ♛ победитель ♛' if pl.isWin else '')) for pl in players]
