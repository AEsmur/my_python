lst = []
print('\nПростой todo:\n1. Добавить задачу.\n2. Вывести список задач.\n3. Выход.')
while True:
    dct = {}
    num = input('\nВведите число: ')
    if num == '1':
        name = input('Сформулируйте задачу: ')
        ctg = input('Добавьте категорию к задаче: ')
        time = input('Добавьте время к задаче: ')
        dct['name'] = name
        dct['category'] = ctg
        dct['time'] = time
        lst.append(dct)
    elif num == '2':
        for i in lst:
            print('Задача:',i['name'],' Категория:',i['category'],
                  ' Дата:',i['time'])
    elif num == '3':
        break
    else:
        print('Введите другое число (1,2 или 3)!!!')
print(dct)
