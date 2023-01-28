# Задание в группах: Создать телефонный справочник с возможностью импорта и экспорта данных в нескольких форматах.

# TODO:
# 1. разбить на модули
# - view
# - controller
# - main
# - models
# 2. добавить функционал для:
#   - редактирования
#   - * поиска
#   - * вывода
# 3. реализовать интерфейс

from Data import Data

data = Data('files/directory.csv', 'csv')
data.view()
# print(data.search('phone', '71-11'))
# data.save('files/directory.txt', 'txt')
