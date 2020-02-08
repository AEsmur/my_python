import math
x = int(input('Введите положительное число (до 15): '))
def pi_sign(x):
    return(f'{math.pi:.{x}f}')
print(pi_sign(x))
