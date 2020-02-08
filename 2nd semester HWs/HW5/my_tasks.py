tasks = []
ctgs = []
times = []
print('\nПростой todo:\n1. Добавить задачу.\n2. Вывести список задач.\n3. Выход.')
while True:
    num = input('\nВведите число: ')
    if num == '1':
        task = input('Сформулируйте задачу: ')
        ctg = input('Добавьте категорию к задаче: ')
        time = input('Добавьте время к задаче: ')
        tasks.append(task)
        ctgs.append(ctg)
        times.append(time)
    elif num == '2':
        for i in range(len(tasks)):
            print('Задача:',tasks[i],' Категория:',ctgs[i],' Дата:',times[i])
    elif num == '3':
        break
    else:
        print('Введите другое число (1,2 или 3)!!!')
