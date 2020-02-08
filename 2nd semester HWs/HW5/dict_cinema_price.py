cinema_d = {'Пятница':  {12: 250, 16: 350, 20: 450},
    'Чемпионы':  {10: 250, 13: 350, 16: 350},
    'Пернатая банда': {10: 350, 14: 450, 18: 450}}
film = str(input('Выбранный фильм: '))
date = str(input('Выбранная дата (сегодня/завтра): '))
time = int(input('Выбранное время сеанса: '))
numb = int(input('Количество билетов: '))
def sale(date, numb):
    if date == 'завтра' and numb >= 20:
        return 0.75
    elif date == 'завтра':
        return 0.95
    elif numb >= 20:
        return 0.8
    else:
        return 1
if film in cinema_d:
    if date == 'сегодня' or date == 'завтра':
        if time in cinema_d[film]:
            print("Выбранный фильм:", film, " День:", date, " Время:", time, " Количество билетов:", numb)
            print('Стоимость билетов составила', cinema_d[film][time] * sale(date, numb) * numb)
        else:
            print('Ошибка ввода')
    else:
        print('Ошибка ввода')
else:
    print('Ошибка ввода')
