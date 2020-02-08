from tkinter import *
import json
from tkinter import messagebox as mb

lst = []


def saved_tasks(): #функция выводит сохранённые ранее (в json-файле) записи                       
    try:
        with open('todo_list.json', 'r', encoding = 'cp1251') as json_file:
            contents = json.load(json_file)
        for todo in contents:
            all_tasks.configure(state = NORMAL)
            all_tasks.insert(1.0, "Задача: " + todo['task'] + " " + "Категория: " + todo[
                'category'] + " " + "Дата: " + todo['time'] + '\n')
            all_tasks.configure(state = DISABLED)
    except Exception as ex:
        print(ex)
        

def write(new_task): #функция для добавления записей в json-файл
    try:
        with open('todo_list.json', 'r', encoding = 'cp1251') as json_file:
            contents = json.load(json_file)
        for i in new_task:
            contents.append(i)
    except Exception as ex:
        print(ex)

    try:
        with open('todo_list.json', 'w', encoding = 'windows-1251') as file_write:
            json.dump(contents, file_write, sort_keys = False, ensure_ascii = False)
    except Exception as e:
        print(e)
        

def add():  # Функция для добавления записей
    dct = {}
    if entry_task.get() != '' and entry_category.get() != '' and entry_time.get() != '':
        dct["task"] = entry_task.get()
        dct["category"] = entry_category.get() 
        dct['time'] = entry_time.get()
        lst.append(dct)
        write(lst)
    elif entry_task.get() == '' and entry_category.get() != '' and entry_time.get() != '':
        mb.showerror("ОШИБКА", "Внимание! Нужно ввести задачу!")
    elif entry_task.get() != '' and entry_category.get() == '' and entry_time.get() != '':
        mb.showerror("ОШИБКА", "Внимание! Нужно ввести категорию!")
    elif entry_task.get() != '' and entry_category.get() != '' and entry_time.get() == '':
        mb.showerror("ОШИБКА", "Внимание! Нужно ввести время!")
    elif entry_task.get() == '' and entry_category.get() == '' and entry_time.get() != '':
        mb.showerror("ОШИБКА", "Внимание! Нужно ввести задачу и категорию!")
    elif entry_task.get() == '' and entry_category.get() != '' and entry_time.get() == '':
        mb.showerror("ОШИБКА", "Внимание! Нужно ввести задачу и время!")
    elif entry_task.get() != '' and entry_category.get() == '' and entry_time.get() == '':
        mb.showerror("ОШИБКА", "Внимание! Нужно ввести категорию и время!")
    else:
        mb.showerror("ОШИБКА", "Внимание! Нужно ввести задачу, категорию и время!")
        
        
def task_list():  # Функция для просмотра списка всех записей
    all_tasks.configure(state = NORMAL)
    all_tasks.delete(1.0, END)
    try:
        all_tasks.grid()
        with open('todo_list.json', 'r', encoding = 'cp1251') as json_file:
            contents = json.load(json_file)
        for todo in contents:
            all_tasks.configure(state = NORMAL)
            all_tasks.insert(1.0, "Задача: " + todo['task'] + " " + "Категория: " + todo[
                'category'] + " " + "Дата: " + todo['time'] + '\n')
            all_tasks.configure(state = DISABLED)

    except:
        with open('todo_list.json', 'r', encoding = 'cp1251') as json_file:
            contents = json.load(json_file)
        for todo in contents:
            all_tasks.configure(state = NORMAL)
            all_tasks.insert(1.0, "Задача: " + str(todo['task']) + " " + "Категория: " + str(todo[
                'category']) + " " + "Дата: " + str(todo['time']) + '\n')
            all_tasks.configure(state = DISABLED)


    all_tasks.configure(state = DISABLED)



root = Tk()
root.title("Менеджер задач")
root.geometry('768x200')
root.resizable(width = False, height = False)

frame_1 = Frame(root, width = 320, height = 120)
frame_2 = Frame(root, width = 350, height = 40)
frame_3 = Frame(root, width = 320, height = 160)

frame_1.place(x = 0, y = 0)
frame_2.place(x = 350, y = 0)
frame_3.place(x = 0, y = 70)


all_tasks = Text(frame_2, width = 40, height = 10, font='Georgia')
all_tasks.grid()

label_task = Label(frame_1, text = 'Задача: ', font='Georgia')
label_task.grid(row = 0, column = 0)

label_category = Label(frame_1, text = 'Категория: ', font='Georgia')
label_category.grid(row = 1, column = 0)

label_time = Label(frame_1, text = 'Время: ', font='Georgia')
label_time.grid(row = 2, column = 0)

entry_task = Entry(frame_1, width = 40)
entry_task.grid(row = 0, column = 1)

entry_category = Entry(frame_1, width = 40)
entry_category.grid(row = 1, column = 1)

entry_time = Entry(frame_1, width = 40)
entry_time.grid(row = 2, column = 1)

button_add = Button(frame_3, text = "Добавить", font='Georgia', width = 15, command = add)
button_add.place(x = 90, y = 5)

button_task_list = Button(frame_3, text = "Список задач", font='Georgia', width = 18, command = task_list)
button_task_list.place(x = 80, y = 40)

button_exit = Button(frame_3, text = "Выход", width = 15, font='Georgia', command = root.destroy)
button_exit.place(x = 90, y = 75)

saved_tasks()

root.mainloop()
