def calc(expr):
    '''
    >>> calc("1 2 + 4 * 3 +")
    '15'
    >>> calc("1 2 3 * + 2 -")
    '5'
    '''
    stack = []
    for i in expr:
        if i.isdigit():
            stack.append(i)
        else:
            if i == '+':
                a = int(stack.pop())
                b = int(stack.pop())
                stack.append(a + b)
            elif i == '-':
                a = int(stack.pop())
                b = int(stack.pop())
                stack.append(b - a)
            elif i == '*':
                a = int(stack.pop())
                b = int(stack.pop())
                stack.append(b * a)
            elif i == '/':
                a = int(stack.pop())
                b = int(stack.pop())
                stack.append(b / a)
    return str(stack[0])

#print(calc("1 2 3 * + 2 -"))

import doctest
doctest.testmod()
