a = int(input('Первое число: '))
b = int(input('Второе число: '))

def max(a, b):
    if a >= b:
        return(a)
    else:
        return(b)

print('Максимальное из них равно', max(a, b))
