from tkinter import *
import math

def evaluate_radius():
    global result_all
    result_all = 0
    try:
        k = int(entry_radius.get())
        if k > 0:
            result = 4/3 * math.pi * k**3
            result_all = round(result, 2)
            label_result.config(text=result_all)
        else:
            label_result.config(text="Неверное значение")
    except ValueError:
        label_result.config(text="Нужно ввести ЧИСЛО")
    try:
        result_all = str(result_all)
    except Exception as ex:
        print(ex)
    
select = "Текст"
def save_file():
    try:
        if select == "Текст":
            writer_txt(result_all)
        else:
            writer_html(result_all)
    except Exception as ex:
        print(ex)

def writer_txt(something):
    try:
        with open('file.txt', 'a') as file:
            file.write(something + "\n")
    except:
        with open('file.txt', 'w', encoding='windows-1251') as file_write:
            file_write.write(something + '\n')

def  writer_html(something):
    try:
        with open('file.html', 'a') as file:
            file.write(something + '\n')
    except:
        with open('file.html', 'w', encoding='windows-1251') as file:
            file.write(something + '\n')


def call_back(selection):
    try:
        global select
        select = selection
    except Exception as ex:
        print(ex)


root = Tk()
root.title("Программа для вычисления объема сферы")

frame1 = Frame(root, width=300, height=127)
frame1.grid()

frame1.grid_propagate(0)

label_radius = Label(frame1, text='Ввести радиус', font='Georgia 8')
label_radius.grid(row=0, column=0, pady=3)

entry_radius = Entry(frame1, width=20)
entry_radius.grid(row=0, column=1, pady=3)

label_result = Label(frame1, text="Результат вычислений", font='Georgia 8')
label_result.grid(row=1, column=0, pady=3)

label_result = Label(frame1, font='Georgia 8')
label_result.grid(row=1, column=1, pady=3)

button_evaluate = Button(frame1, text="Вычислить", font='Georgia 8', command=evaluate_radius)
button_evaluate.grid(row=2, column=0, pady=3)

button_save = Button(frame1, text="Сохранить", font='Georgia 8',command=save_file)
button_save.grid(row=3, column=0, pady=3)

vat = StringVar()

option_menu = OptionMenu(frame1,vat,"Текст", "HTML", command=call_back)
option_menu.grid(row=3, column=1)
vat.set("Текст")



root.resizable(width=False, height=False)
root.mainloop()
