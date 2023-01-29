import copy
import math
import os

from logDebug import logDebug
from fileUsage import fileUsage
from dataHandler import dataHandler


class main:
    __log = logDebug()

    __fileName = 'data'
    __fileUsage = fileUsage()
    __dataHandler = dataHandler()

    __dataCountInPage = 20

    data = []

    def __init__(self):
        try:
            self.load()
            # self.save('files/test_file.csv')
        except Exception as e:
            self.__log.new(e)

    def load(self, f='csv'):
        text = self.__fileUsage.load(f'{self.__fileName}.{f}')  # Считываем файл
        data = self.__dataHandler.textToData(text, f)  # Загружаем данные
        self.data = data

    def save(self, file=None, f='csv'):
        file = file if file is not None else self.__fileName
        text = self.__dataHandler.dataToText(self.data, f)  # Формируем файл для записи
        self.__fileUsage.save(f'{file}.{f}', text)  # Сохраняем файл

    def viewData(self, record=None, page=1):  # Отображение данных
        # TODO переработать после доработки индексов
        if record is None:
            __count = self.__dataCountInPage
            __start = (page - 1) * __count
            __end = __start + __count
            __data = self.data[__start:__end]
            __maxLen = [len(__item) for __item in __data[0].keys()]
            for __record in __data:
                __maxLen = [
                    len(str(__item)) if len(str(__item)) > __maxLen[__key] else __maxLen[__key]
                    for __key, __item in enumerate(__record.values())
                ]
            __lineLen = sum(__maxLen) + len(__data[0].keys()) * 3 - 1
            __thisPage = f'Страница {page} из {math.ceil(len(self.data) / __count)}'
            print('-' * __lineLen)
            print(' ' + ' | '.join(
                __item.ljust(__maxLen[__key]) for __key, __item in enumerate(__data[0].keys())
            ) + ' ')
            print('-' * __lineLen)
            [print(' ' + ' | '.join([
                str(__field).ljust(__maxLen[__key])
                for __key, __field in enumerate(__item.values())
            ]) + ' ') for __item in __data]
            print('--- ' + __thisPage + ' ' + '-' * (__lineLen - len(__thisPage) - 5))
        else:
            __data = record
            __maxLen = [
                max([len(__key) for __key in __data.keys()]),  # name
                max([len(str(__value)) for __value in __data.values()])  # value
            ]
            __lineLen = sum(__maxLen) + 3
            __name = f'Запись #{__data.id()}'
            print('--- ' + __name + ' ' + '-' * (__lineLen - len(__name) + 2))
            for __num, __item in enumerate(__data.keys()):
                if __item == 'idx':
                    continue
                print(f'{__num} - {str(__item)}{str(__data.get(__item)).rjust(__lineLen - len(__item) + 3, ".")}')
            print('-' * (__lineLen + 7))

    def searchData(self):
        # TODO Доделать поиск
        pass

    def addData(self):
        __newData = self.__editForm(self.__dataHandler.model())
        self.data.append(__newData)

    def editData(self, idx):
        __newData = self.__editForm(self.data[idx])
        for __key in __newData.keys():
            self.data[idx].set(__key, __newData.get(__key))

    def delData(self, idx):
        # TODO придумать что-нибудь с индексами
        try:
            if self.data[idx].id() == idx:
                # del self.data[idx]
                self.data[idx] = None
            else:
                raise IndexError()
        except IndexError:
            print('Запись не найдена')

    def __editForm(self, record=None):  # Редактирование данных
        __newData = copy.deepcopy(record)
        __boolVal = {
            True: ['1', 'Y', 'y', 'Yes', 'yes', 'Д', 'д', 'Да', 'да'],
            False: ['0', 'N', 'n', 'No', 'no', 'Н', 'н', 'Нет', 'нет']
        }
        isBool = lambda x: True in [x in __boolVal[__item] for __item in __boolVal]
        boolVal = lambda x: True if x in __boolVal[True] else False
        __exit = False
        while not __exit:
            self.viewData(__newData)

            __num = 0
            while not 0 < __num < len(__newData.keys()):
                __num = int(input('Выберите поле для редактирования: '))

            __key = __newData.keys()[__num]
            __value = __newData.get(__key)

            __newData.set(__key, input(f'[{__key}: {__value}] На что меняем: '))

            __exitValue = None
            while not isBool(__exitValue):
                __exitValue = input('Закончить редактирование? (Y/N) ')
            __exit = boolVal(__exitValue)

        self.viewData(__newData)
        __saveValue = None
        while not isBool(__saveValue):
            __saveValue = input('Сохранить изменения? (Y/N) ')
        return __newData if boolVal(__saveValue) else record

    def __exit(self):
        self.save()
        exit()

    def menu(self):
        __menu = {
            1: {
                'name': 'Вывести список сотрудников',
                'function': lambda: self.viewData(page=int(input(
                    f'Вывести страницу (из {math.ceil(len(self.data) / self.__dataCountInPage)}): ')
                ))
            },
            2: {
                'name': 'Найти сотрудника',
                'function': lambda: False
            },
            3: {
                'name': 'Добавить сотрудника',
                'function': lambda: self.addData()
            },
            4: {
                'name': 'Редактировать сотрудника',
                'function': lambda: self.editData(int(input('Введите idx записи: ')))
            },
            5: {
                'name': 'Удалить сотрудника',
                'function': lambda: self.delData(int(input('Введите idx записи: ')))
            },
            6: {
                'name': 'Экспортировать данные в csv',
                'function': lambda: self.save(input('Введите имя файла: '))
            },
            7: {
                'name': 'Закончить работу',
                'function': lambda: self.__exit()
            }
        }
        print('-' * 20)
        [print(f'{__item} - {__menu[__item]["name"]}') for __item in __menu]
        print('-' * 20)
        try:
            __item = int(input('Выберите номер действия: '))
            __menu[__item]['function']()
            os.system('cls||clear')
        except KeyError as key:
            self.__log.new(f'Введенный ключ ({key}) не найден')
        except Exception as e:
            self.__log.new(e)
