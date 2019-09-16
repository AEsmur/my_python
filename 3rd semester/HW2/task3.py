import tkinter

class MyGui:
    def __init__(self):
        self.main_window = tkinter.Tk()
        
        self.top_frame = tkinter.Frame()
        self.top2_frame = tkinter.Frame()
        self.bottom_frame = tkinter.Frame()
        self.bottom2_frame = tkinter.Frame()
        
        self.value = tkinter.StringVar()
        
        self.gal_label = tkinter.Label(self.top_frame, text='Введите кол-во галлонов:')
        self.gal_entry = tkinter.Entry(self.top_frame, width=10)
        self.mil_label = tkinter.Label(self.top2_frame, text='Введите кол-во миль:')
        self.mil_entry = tkinter.Entry(self.top2_frame, width=10)
        self.res_text = tkinter.Label(self.bottom_frame, text = "Мили на галлон (MPG) = ")
        self.res = tkinter.Label(self.bottom_frame, textvariable = self.value)
        self.calc_button = tkinter.Button(self.bottom2_frame, text = 'Преобразовать', command=self.convert)
        self.quit_button = tkinter.Button(self.bottom2_frame, text = 'Выйти', command=self.main_window.destroy)
        
        self.gal_label.pack(side = "left")
        self.gal_entry.pack(side = "right")
        self.mil_label.pack(side = "left")
        self.mil_entry.pack(side = "right")
        self.res_text.pack(side = "left")
        self.res.pack()
        self.calc_button.pack(side = "left")
        self.quit_button.pack()
        
        self.top_frame.pack()
        self.top2_frame.pack()
        self.bottom_frame.pack()
        self.bottom2_frame.pack()
        
        tkinter.mainloop()
        
    
    def convert(self):
        try:
            txt = round(int(self.mil_entry.get()) / int(self.gal_entry.get()),
                        ndigits = 3)
        except:
            txt = "Error!"
        self.value.set(txt)
a = MyGui()
