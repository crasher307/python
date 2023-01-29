class dataObj(object):
    def __init__(self, idx, data):
        self.idx = idx
        self.__keys = []
        self.__values = []
        for key in data:
            self.__setattr__(key, data[key])
            self.__keys.append(key)
            self.__values.append(data[key])

    def keys(self):
        return ['idx'] + self.__keys

    def values(self):
        return [self.idx] + self.__values

    def id(self):
        return self.idx

    def get(self, key):
        return self.__getattribute__(key)

    def set(self, key, value):
        if key == 'idx':
            return
        __key = list(filter(lambda x: x is not None, [k if v == key else None for k, v in enumerate(self.__keys)]))[0]
        self.__values[__key] = value
        self.__setattr__(key, value)


class dataHandler:
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

    __lastIdx = 0
    __keys = None

    # __model = None

    def __assoc(self, k, v):
        return {d[0]: d[1] for d in list(filter(lambda x: x[0] is not None, zip(k, v)))}

    def model(self):
        self.__lastIdx += 1
        return dataObj(self.__lastIdx, self.__assoc(self.__keys, ['' for i in self.__keys]))

    # file to [dataObj(), ...]
    def textToData(self, data, f):  # Вычитка данных в массив объектов
        try:
            __format = self.__format[f]
            __row = __format['row']
            __field = __format['field']

            __items = data.strip(__row).split(__row)
            __keys = [__key if __key else None for __key in __items[0].split(__field)]
            __data = [self.__assoc(__keys, __values) for __values in [__item.split(__field) for __item in __items[1::]]]

            __response = [dataObj(__idx, __record) for __idx, __record in enumerate(__data)]
            self.__keys = __keys
            self.__lastIdx = __response[-1].id()

            return __response
        except Exception as __error:
            raise Exception(__error)

    # [dataObj(), ...] to file
    def dataToText(self, data, f):  # Преобразование массива объектов в формат для записи (def: CSV)
        try:
            __format = self.__format[f]
            __row = __format['row']
            __field = __format['field']

            __data = [data[0].keys()] + [__item.values() for __item in data]
            __data = __row.join([__field.join(list(map(str, __item))) for __item in __data])
            __data += '\n'

            return __data
        except Exception as __error:
            raise Exception(__error)
