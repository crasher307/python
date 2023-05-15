from datetime import datetime


# Заметка
class Note:
    __idx = None
    __title = None
    __body = None
    __update = None

    def get_idx(self):
        return self.__idx

    def get_title(self):
        return self.__title

    def get_body(self):
        return self.__body

    def get_update(self):
        return self.__update

    def __init__(self, idx, title=None, body=None, date=None):
        self.__idx = idx
        self.__title = '' if title is None else title
        self.__body = '' if body is None else body
        self.__update = self.__stamp() if date is None else date

    def update(self, title, body):
        self.__title = title
        self.__body = body
        self.__update = self.__stamp()

    def __stamp(self):
        return datetime.strftime(datetime.today(), '%Y-%m-%d %H:%M:%S.%f')[:23]
