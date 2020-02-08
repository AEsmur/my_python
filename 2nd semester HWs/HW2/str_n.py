s = input('Введите строку: ')
n = int(input('Введите целое число: '))
def str_n(s,n):
    if len(s) > n:
        return(s.upper())
    else:
        return(s)
print(str_n(s,n))
