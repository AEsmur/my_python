def calc(num1, num2, oper):
    dict = {'+': lambda num1, num2: num1 + num2,
            '-': lambda num1, num2: num1 - num2,
            '*': lambda num1, num2: num1 * num2,
            '^': lambda num1, num2: num1 ** num2,
            '/': lambda num1, num2: num1 / num2}
    return dict[oper](num1,num2)
try:
    num1 = float(input('Введите первое число: '))
    num2 = float(input('Введите второе число: '))
    oper = input('Введите оператор: ')
    print(calc(num1, num2, oper))
except ZeroDivisionError:
    print('При выполнении программы происходит деление на ноль')
except ValueError:
    print('При выполнении программы происходит неверное преобразование типа.',
          'Введите ЧИСЛО!')
except KeyError:
    print('При выполнении программы происходит ввод неверного оператора.',
          "Введите один из операторов: '+','-','*','^','/'")
