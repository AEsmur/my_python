import math
x = float(input('Введите число: '))
def sinus(x):
    if 0.2 <= x <= 0.9:
        return math.sin(x)
    else:
        return 1
print('Значение функции в данной точке равно',sinus(x))
