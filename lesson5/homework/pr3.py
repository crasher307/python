# Создайте программу для игры в "Крестики-нолики".

class game:
    __fields = None
    __chars = None
    __win = [
        [1, 2, 3], [4, 5, 6], [7, 8, 9],
        [1, 4, 7], [2, 5, 8], [3, 6, 9],
        [1, 5, 9], [3, 5, 7]
    ]

    def view(self):
        print('-----------')
        [print(
            f'{f" {k} " if self.__fields[k] == "-" else f"-{self.__fields[k]}-"}',
            end=('|' if k % 3 else '\n')
        ) for k in self.__fields]
        print('-----------')

    def setVal(self, c):
        while True:
            try:
                i = int(input(f'Куда вводим {c}: '))
                if self.__fields[i] == '-':
                    self.__fields[i] = c
                else:
                    print('Ячейка уже заполнена')
                    continue
                break
            except (KeyError, ValueError):
                print('Ошибка ввода, попробуйте снова')

    def isWin(self):
        winner = False
        for w in self.__win:
            for ch in self.__chars:
                winner = f'Победитель {ch}' if [self.__fields[i] for i in w].count(ch) == len(w) else winner
        if not winner and '-' not in [self.__fields[i] for i in self.__fields]:
            winner = 'Ничья'
        return winner

    def start(self):
        self.__fields = {i: '-' for i in range(1, pow(3, 2) + 1)}
        self.__chars = ['X', 'O']
        while not self.isWin():
            self.view()
            self.setVal(self.__chars[0])
            self.__chars.reverse()
        else:
            self.view()
            print(self.isWin())


game().start()