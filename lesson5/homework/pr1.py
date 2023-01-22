# Напишите программу, удаляющую из текста все слова, содержащие "абв".

check = lambda s: True not in [need in s.lower() for need in ['а', 'б', 'в']]

text = 'Привет, это простой текст содержащий "абв" слова, которые в последствии будут удалены'
lst = " ".join(list(filter(check, text.split())))

print(f'Base:\t{text}\nResult:\t{lst}')
