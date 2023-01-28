import datetime
import math
import traceback


class Data:
    __debugMode = False
    __logFile = 'files/log.txt'

    __file = None
    __encoding = 'cp1251'
    __format = {
        'csv': {  # format
            'row': '\n',  # row_separator
            'field': ';'  # field_separator
        },
        'txt': {
            'row': '\n',
            'field': '--'
        }
    }

    keys = []
    data = []

    def view(self):
        __count = None
        __page = None
        while True:
            try:
                __rd = input(
                    '"exit" - выход\n' +
                    ('Сколько записей выводить на странице: ' if not __count else 'Отобразить страницу: ')
                )
                if __rd == 'exit':
                    break
                __rd = int(__rd)
                if __rd < 1:
                    raise ValueError()
                if not __count:
                    __count = __rd
                else:
                    __page = __rd
                    self.__viewAll(__page, __count)
            except ValueError:
                print('[Ошибка] Введите корректное число')
            except Exception as __err:
                self.__log(__err)

    def search(self, key, value):
        return list(filter(lambda x: str(value) in x[key], self.data))

    def __init__(self, file, f='csv'):  # Инициализация (считывание файла)
        self.__isInit = False
        self.__file = file
        try:
            __format = self.__format[f]
            self.__dataGet(self.__fileRead(), __format['row'], __format['field'])
        except KeyError as __key:
            self.__log(f'Формат {__key} не задан, выберите из установленных {list(self.__format.keys())}')
        except Exception as __err:
            self.__log(__err)

    def save(self, file, f='csv'):  # Сохранение данных в файл
        try:
            __format = self.__format[f]
            if not self.__fileWrite(file, self.__dataSet(self.keys, self.data, __format['row'], __format['field'])):
                raise Exception('Ошибка записи в файл')
        except KeyError as __key:
            self.__log(f'Формат {__key} не задан, выберите из установленных {list(self.__format.keys())}')
        except Exception as __err:
            self.__log(__err)

    '''
    *** Для внутреннего пользования ***
    '''

    def __viewAll(self, page, count):  # Вывод данных
        __maxLen = []
        __start = (page - 1) * count
        __end = __start + count
        for __item in self.data[__start:__end]:
            for __f, __v in enumerate(__item):
                __len = len(__item[__v]) if __item[__v] else 0
                try:
                    __maxLen[__f] = __maxLen[__f] if __maxLen[__f] >= __len else __len
                except IndexError:
                    __maxLen.append(len(self.keys[__f]))
        print('\n'.join(
            [' | '.join([
                str(__k).ljust(__maxLen[__i]) for __i, __k in enumerate(self.keys)
            ])] + [' | '.join([
                str(__item[__k] if __item[__k] else '').ljust(__maxLen[__i]) for __i, __k in enumerate(__item)
            ]) for __item in self.data[__start:__end]] + [
                f'--- Страница {page} из {math.ceil(len(self.data) / count)} ---'
            ]
        ))

    def __fileRead(self):  # Считывание файла
        try:
            __data = None
            with open(self.__file, 'r', encoding=self.__encoding) as __f:
                __data = __f.read()
            return __data
        except Exception as __err:
            self.__log(__err)
            return False

    def __fileWrite(self, file, text):  # Запись файла
        try:
            if not text:
                raise Exception('Ошибка формирования данных для записи в файл')
            with open(file, 'w', encoding=self.__encoding) as __f:
                result = __f.write(text)
            return result
        except Exception as __err:
            self.__log(__err)
            return False

    # file to data[{ ... }, ...]
    def __dataGet(self, data, row, field):  # Преобразование считанных данных в массив объектов
        try:
            __data = data.strip(row).split(row)
            __keys = [__key if __key else None for __key in __data[0].split(field)]
            __items = [[__item if __item else None for __item in __d.split(field)] for __d in __data[1::]]
            self.keys = list(filter(lambda x: x is not None, __keys))
            for __obj in [list(zip(__keys, __values)) for __values in __items]:
                self.data.append({__f[0]: __f[1] for __f in list(filter(lambda x: x[0] is not None, __obj))})
            return True
        except Exception as __err:
            self.__log(__err)
            return False

    # data[{ ... }, ...] to file
    def __dataSet(self, keys, data, row, field):  # Преобразование массива объектов в формат для записи (def: CSV)
        try:
            __data = []
            for __obj in self.data:
                __data.append(field.join([item if item is not None else '' for item in __obj.values()]))
            __data = f'{row.join([field.join(self.keys)] + __data)}{row}'
            return __data
        except Exception as __err:
            self.__log(__err)
            return False

    def __log(self, err):  # Логирование ошибок
        __mess = [] if self.__isInit else [f'Цикл от {datetime.datetime.today()}']
        __mess += [f'\t{__s}' for __s in f'Error: {err}'.split('\n')]
        if type(err) == TypeError:
            __mess += ['\tTraceback:'] + [
                '\t\t' + ', '.join(list(__s.strip() for __s in __item.split('\n'))).strip(', ')
                for __item in traceback.format_stack()[:-1:]
            ]
        __mess = '\n'.join(__mess)
        with open(self.__logFile, 'a+', encoding='utf-8') as __f:
            __f.write(__mess + '\n\n')
        self.__isInit = self.__isInit if self.__isInit else True
        print(f'*** DEBUG ***\n{__mess}') if self.__debugMode else False