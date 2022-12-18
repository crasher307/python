# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

week = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']
weekEnd = False
day = None

dayName = None
while dayName is None:
    day = int(input('Введите номер дня недели: ')) - 1
    try:
        dayName = week[day] if day >= 0 else None
        if dayName is None:
            print(f'Попробуйте снова')
    except Exception as err:
        print(f'Попробуйте снова ({err})')

weekEnd = 'выходной' if day > 4 else 'рабочий день'
print(f'{dayName} ({weekEnd})')
