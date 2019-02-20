film = str(input('Выбранный фильм: '))
date = str(input('Выбранная дата (сегодня/завтра): '))
time = int(input('Выбранное время сеанса: '))
numb = int(input('Количество билетов: '))

def price(film, time):
    if film == 'Пятница':
        if time == 12:
            return 250
        elif time == 16:
            return 350
        elif time == 20:
            return 450
        else:
            return 0
    elif film == 'Чемпионы':
        if time == 10:
            return 250
        elif time == 13:
            return 350
        elif time == 16:
            return 350
        else:
            return 0
    elif film == 'Пернатая банда':
        if time == 10:
            return 350
        elif time == 14:
            return 450
        elif time == 18:
            return 450
        else:
            return 0
    else:
        return 0

def sale(date, numb):
    if date == 'завтра' and numb >= 20:
        return 0.75
    elif date == 'завтра':
        return 0.95
    elif numb >= 20:
        return 0.8
    else:
        return 1

if price(film,time) != 0:
    print('Стоимость билетов составила', price(film, time) * sale(date, numb) * numb)
else:
    print('Ошибка ввода')
