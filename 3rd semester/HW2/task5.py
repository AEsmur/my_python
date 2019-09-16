import tkinter
import tkinter.messagebox

class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        self.top_frame.pack()
        self.bottom_frame.pack()

        self.var = tkinter.IntVar()
        self.var.set(1)

        self.rb1 = tkinter.Radiobutton(self.top_frame,text='Дневное время (6:00 - 17:59)',
                                                 variable=self.var, value=1)
        self.rb2 = tkinter.Radiobutton(self.top_frame, text='Вечернее время (18:00 - 23:59)',
                                                 variable=self.var, value=2)
        self.rb3 = tkinter.Radiobutton(self.top_frame, text='Непиковый период (00:00 - 5:59)',
                                                 variable=self.var, value=3)
        self.label = tkinter.Label(self.top_frame, text='Введите количество минут: ')
        self.entry = tkinter.Entry(self.top_frame, width=10)

        self.button_1 = tkinter.Button(self.bottom_frame, text='Показать стоимость',
                                       command=self.summary)
        self.button_2 = tkinter.Button(self.bottom_frame, text='Выйти',
                                       command=self.main_window.destroy)
        
        self.rb1.pack()
        self.rb2.pack()
        self.rb3.pack()
        self.label.pack(side='left')
        self.entry.pack()

        self.button_1.pack(side='left')
        self.button_2.pack()
        
        tkinter.mainloop()

    def summary(self):
        summ = 0
        self.message = 'Ваши затраты = $'
        
        if str(self.var.get()) == str(1):
            summ = round(0.1 * int(self.entry.get()), 2)
        if str(self.var.get()) == str(2):
            summ = round(0.12 * int(self.entry.get()), 2)
        if str(self.var.get()) == str(3):
            summ = round(0.05 * int(self.entry.get()), 2)
        self.message += str(summ)

        tkinter.messagebox.showinfo("Общая стоимость", self.message)

a = MyGUI()
