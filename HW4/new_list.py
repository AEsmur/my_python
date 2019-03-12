from math import sqrt

#через цикл for
a = [2,4,9,16,25]
for i in range(len(a)):
    a[i] = sqrt(a[i])
print(a)

#через map
a = [2,4,9,16,25]
b = list(map(sqrt,a))
print(b)

#в виде генератора списка
a = [2,4,9,16,25]
b = [sqrt(i) for i in a]
print(b)
