from controlWork.Note import Note


# Список заметок
class Notes:
    __file = 'notes.csv'
    __data = []

    def get_data(self, idx=None):
        __view = None
        try:
            self.sort(True)
            if idx is None:
                __view = self.__data
            else:
                __view = list(filter(lambda __item: __item.get_idx() == idx, self.__data))
                __view = __view[0] if len(__view) > 0 else None
                if __view is None:
                    raise Exception(f'Заметка с [id: {idx}] не найдена')
        except Exception as __err:
            print(f'Error: {__err}')
        return __view

    # Добавление заметки
    def add(self, title=None, body=None, idx=None, update=None, load=False):
        try:
            self.sort()
            __lastIdx = self.__data[-1].get_idx() + 1 if len(self.__data) > 0 else 0
            self.__data.append(Note(__lastIdx if idx is None else int(idx), title, body, update))
            if not load:
                self.save()
        except Exception as __err:
            print(f'Error: {__err}')

    # Редактирование заметки
    def update(self, idx=None, title=None, body=None):
        if idx is None:
            return
        try:
            self.sort()
            __upd = list(filter(lambda __item: __item.get_idx() == idx, self.__data))
            if len(__upd) > 0:
                __upd[0].update(title, body)
                self.save()
            else:
                raise Exception(f'Заметка с [id: {idx}] не найдена')
        except Exception as __err:
            print(f'Error: {__err}')

    # Удаление заметки
    def remove(self, idx=None):
        if idx is None:
            return
        try:
            self.sort()
            __del = list(filter(lambda __item: __item.get_idx() == idx, self.__data))
            if len(__del) > 0:
                self.__data.remove(__del[0])
                self.save()
            else:
                raise Exception(f'Заметка с [id: {idx}] не найдена')
        except Exception as __err:
            print(f'Error: {__err}')

    # Сортировка
    def sort(self, update=False):
        self.__data.sort(key=(Note.get_update if update else Note.get_idx), reverse=update)

    # Загрузка заметок
    def load(self):
        try:
            with open(self.__file, 'r', encoding='cp1251') as __f:
                __data = __f.read()
            __data = list(filter(lambda x: x != '', __data.split('\n')))
            __values = [__item.split(';') for __item in __data]
            for __obj in __values:
                self.add(__obj[1], __obj[2], __obj[0], __obj[3], True)
        except Exception as __err:
            print(f'Error: {__err}')

    # Сохранение заметок
    def save(self):
        try:
            __data = '\n'.join([
                f'{__item.get_idx()};{__item.get_title()};{__item.get_body()};{__item.get_update()}'
                for __item in self.__data
            ])
            if not __data:
                raise Exception('Отсутствуют данные для записи')
            with open(self.__file, 'w', encoding='cp1251') as __f:
                __f.write(__data)
        except Exception as __err:
            print(f'Error: {__err}')
