from controlWork.Notes import Notes


# Приложение
class App:
    exit = False
    __notes = Notes()

    def __init__(self):
        self.__notes.load()

    # Отображение меню
    def menu(self):
        __pause = lambda: input('Нажмите ENTER чтобы продолжить\n')
        __menu = [
            {
                'name': 'Отобразить',
                'func': lambda: self.view(int(input('Введите ID заметки: '))),
                'pause': True
            },
            {
                'name': 'Создать',
                'func': lambda: self.__notes.add(input('Введите заголовок: '), input('Введите заметку: ')),
                'pause': False
            },
            {
                'name': 'Редактировать',
                'func': lambda: self.edit(int(input('Введите ID заметки: '))),
                'pause': True
            },
            {
                'name': 'Удалить',
                'func': lambda: self.__notes.remove(int(input('Введите ID заметки: '))),
                'pause': False
            },
            {
                'name': 'Выйти',
                'func': lambda: self.die(),
                'pause': False
            }
        ]
        __actions = ' | '.join([f'{i} - {item.get("name")}' for i, item in enumerate(__menu)])
        try:
            __action = int(input(f'Выберите действие [ {__actions} ]: '))
            [item.get('func')() if __action == i else None for i, item in enumerate(__menu)]
            if __menu.__getitem__(__action).get('pause'):
                input('Нажмите ENTER чтобы продолжить')
                print()
        except Exception:
            pass

    # Отображение списка заметок
    def list(self):
        try:
            __data = self.__notes.get_data()
            print(
                f'{"-_ID_заметки_-":14s} | {"-_Заголовок_-":40s} | {"-_Дата_обновления_-"}'
                .replace(' ', '-')
                .replace('-|-', ' | ')
                .replace('_', ' ')
                .ljust(120, '-')
            )
            [print(f'{item.get_idx():14d} | {item.get_title():40s} | {item.get_update()}') for item in __data]
            print(''.ljust(120, '-'))
        except Exception as __err:
            print(f'Error: {__err}')

    # Отображение заметки
    def view(self, idx=None):
        if idx is None:
            return
        try:
            __data = self.__notes.get_data(idx)
            if __data is not None:
                __fields = {
                    'Заголовок': __data.get_title(),
                    'Заметка': __data.get_body(),
                    'Изменено': __data.get_update()
                }
                print()
                print(f'Заметка #{idx}')
                [print(f'{item:16} {__fields[item]}') for item in __fields]
                print()
        except Exception as __err:
            print(f'Error: {__err}')

    # Редактирование заметки
    def edit(self, idx):
        __data = self.__notes.get_data(idx)
        if __data is not None:
            print(f'Старый заголовок: {__data.get_title()}')
            __title = input(f'Введите новый заголовок: ')
            print(f'Старая заметка: {__data.get_body()}')
            __body = input('Введите новую заметку: ')
            self.__notes.update(
                idx,
                __title if len(__title) > 0 else __data.get_title(),
                __body if len(__body) > 0 else __data.get_body()
            )
            self.view(idx)

    # Выход
    def die(self):
        self.exit = True


app = App()
while not app.exit:
    app.list()
    app.menu()
