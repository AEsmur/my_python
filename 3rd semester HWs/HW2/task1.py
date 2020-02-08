import tkinter

class MyGui:
    def __init__(self):
        self.main_window = tkinter.Tk()
        
        self.top_frame = tkinter.Frame()
        self.bottom_frame = tkinter.Frame()
        
        self.value = tkinter.StringVar()
        
        self.label = tkinter.Label(self.top_frame, textvariable = self.value)
        self.my_button = tkinter.Button(self.bottom_frame, text = 'Показать инфо', command = self.text)
        self.quit_button = tkinter.Button(self.bottom_frame, text = 'Выйти', command = self.main_window.destroy)
        
        self.label.pack()
        self.my_button.pack(side = "left")
        self.quit_button.pack(side = "right")
        
        self.top_frame.pack()
        self.bottom_frame.pack()
        
        tkinter.mainloop()
    
    def text(self):
        txt = 'Hello world!!!\n' + "I've completed this task"
        self.value.set(txt)
        
a = MyGui()
