# Задание в группах: Создать телефонный справочник с возможностью импорта и экспорта данных в нескольких форматах.

# Разбить на модули:
# - view
# - controller
# - main
# - models

# !!! Было решено сделать в виде класса для работы с файлами,
# тк. в дальнейшем возможны доработки и использование в своих целях

# TODO:
# 1. разбить на модули
# 2. добавить функционал для редактирования
# 3. реализовать интерфейс

from useFile import useFile

file = useFile('pr1/directory.csv', 'csv')
file.view()
