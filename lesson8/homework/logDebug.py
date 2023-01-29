from os import mkdir
from datetime import datetime
from traceback import format_stack as trace


class logDebug:
    __file = 'files/log.txt'
    __encoding = 'utf-8'
    __format = {
        'stamp': '%Y-%m-%dT%H:%M:%S.%f',
        'datetime': '%Y-%m-%dT%H:%M:%S',
        'date': '%Y-%m-%d',
        'time': '%H:%M:%S',
        'timestamp': '%H:%M:%S.%f'
    }
    __isDebug = True
    __isInit = False

    def new(self, e):  # Логирование ошибок
        if not self.__isInit:
            if self.__start() is False:
                mkdir('files')
                self.__start()
            self.__isInit = True
        text = [f'\t{row}' for row in f'--- {self.__stamp("timestamp")[:12]} ---\nMessage: {e}'.split('\n')]
        if type(e) == TypeError:
            text += ['\tTraceback:'] + [
                '\t\t' + ', '.join(list(row.strip() for row in t.split('\n'))).strip(', ')
                for t in trace()
            ]
        text = '\n'.join(text)
        with open(self.__file, 'a+', encoding=self.__encoding) as f:
            f.write(text + '\n\n')
        print(f'*** DEBUG ***\n{text}') if self.__isDebug else False

    def __init__(self, f=None):
        self.__file = self.__file if f is None else f

    def __start(self):
        try:
            with open(self.__file, 'a+', encoding=self.__encoding) as f:
                f.write(f'--- Start: {self.__stamp("datetime")} ---\n\n')
            return True
        except FileNotFoundError:
            return False

    def __stamp(self, f):
        return datetime.strftime(datetime.today(), self.__format[f])
