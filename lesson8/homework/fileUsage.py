import os


class fileUsage:
    __encoding = 'cp1251'
    __dir = os.getcwd().replace('\\', '/') + '/files/'

    def load(self, file):
        try:
            with open(f'{self.__dir}{file}', 'r', encoding=self.__encoding) as f:
                data = f.read()
            return data
        except Exception as error:
            raise Exception(error)

    def save(self, file, data):
        try:
            if not data:
                raise Exception('Отсутствуют данные для записи')
            with open(f'{self.__dir}{file}', 'w', encoding=self.__encoding) as f:
                f.write(data)
            return True
        except Exception as error:
            raise Exception(error)
