import random


class Quotes:
    __file = 'quotes.txt'
    __data = []

    def __load(self):
        with open(self.__file, 'r', encoding='utf-8') as __f:
            __res = __f.read()
        return __res

    def __setData(self):
        __res = []
        for item in str(self.__load()).split('\n'):
            __data = item.split(', – ')
            try:
                __res.append({
                    'text': __data[0],
                    'author': __data[1]
                })
            except IndexError:
                pass
        return __res

    def __init__(self):
        self.__data = self.__setData()

    def data(self):
        return self.__data

    def rand(self):
        return self.__data[random.randint(0, len(self.__data) - 1)]
