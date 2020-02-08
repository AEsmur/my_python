with open('temper.txt','r') as f:
    contents = f.read()
lst = []
for i in contents.split():
    lst.append(float(i))
print('Максимальное значение:', max(lst),'\nМинимальное значение:', min(lst),
      '\nСредняя температура:', round(sum(lst)/len(lst),3),
      '\nКоличество уникальных температур:', len(set(lst)))
