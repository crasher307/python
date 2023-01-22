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
    length = 6

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
    __lastCount = 0
    isBot = True
    isWin = False
    playerName = None

    def __init__(self, descObject, name='Bot'):
        self.__descObject = descObject
        self.playerName = name
        self.isBot = False if 'bot' not in name.lower() else True

    def __call__(self, count=None):
        if count is not None:
            if self.__descObject(count) is False:
                print(f'Некорректное значение, введите от {self.__descObject.min()} до {self.__descObject.max()}')
                return False
            self.__lastCount = count
            self.__countCandy += count
            if self.__descObject.max() == 0:
                self.isWin = True
        return self.__countCandy

    def lastCount(self):
        lc = self.__lastCount
        self.__lastCount = 0
        return lc


def readInput(func, message):
    try:
        return func(input(message))
    except ValueError:
        return False


def botSet(cnd, d=2):
    res = [
        random.randint(cnd.min(), cnd.max()),  # легкий
        cnd() % cnd.max() if cnd() // cnd.max() > 1 else cnd() - (cnd.max() + 1),  # средний
        cnd() % (cnd.max() + 1)  # сложный
    ][d if 0 <= d <= 2 else 2]
    res = res if res >= cnd.min() else cnd.min()
    res = res if res <= cnd.max() else cnd.max()
    return res


desc = Candy()
difficulty = readInput(int, 'Введите сложность (0-2): ')
players = [
    Player(desc, input('Введите имя (ex: player1): ')),
    Player(desc, input('Введите имя (ex: bot): '))
]
candys = lambda c: f'{str(c()).ljust(desc.length, " ")} +{c.lastCount()}'
playerInfo = lambda p: f'\t{candys(p)}\t{p.playerName}' + (' ♛ победитель ♛' if p.isWin else '')
while desc() > 0:
    for pl in players:
        if desc() <= 0:
            continue
        nextPlayer = False
        while nextPlayer is False:
            msg = f'На столе {desc()} конфет, сколько берем [{desc.min()}..{desc.max()}]: '
            cnt = botSet(desc, difficulty) if pl.isBot else readInput(int, msg)
            nextPlayer = pl(cnt) is not False
    print(f'Конфет у игроков:')
    [print(playerInfo(pl)) for pl in players]
