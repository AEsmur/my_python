x = int(input('Введите число: '))

def parity(x):
    if x % 2 == 0:
        return('Чётное')
    else:
        return('Нечётное')        

print(parity(x))
