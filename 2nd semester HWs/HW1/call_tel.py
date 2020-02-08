code = int(input('Код города: '))
talk_len = int(input('Длительность разговора(в минутах): '))

def price(code, talk_len):
    if code == 343:
        return 15 * talk_len
    elif code == 381:
        return 18 * talk_len
    elif code == 473:
        return 13 * talk_len
    elif code == 485:
        return 11 * talk_len
    else:
        print('Укажите другой код')

print('Стоимость разговора составила', price(code, talk_len), 'рублей')
