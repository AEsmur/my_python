import tkinter

class MyGui:
    def __init__(self):
        self.main_window = tkinter.Tk()
        
        self.top_frame = tkinter.Frame()
        self.bottom_frame = tkinter.Frame()
        
        self.value = tkinter.StringVar()
        
        self.label = tkinter.Label(self.top_frame, textvariable = self.value)
        self.sin_button = tkinter.Button(self.bottom_frame, text = 'Sinister', command = self.textL)
        self.dex_button = tkinter.Button(self.bottom_frame, text = 'Dexter', command = self.textR)
        self.med_button = tkinter.Button(self.bottom_frame, text = 'Medium', command = self.textM)
        
        self.label.pack()
        self.sin_button.pack(side = "left")
        self.dex_button.pack(side = "left")
        self.med_button.pack()
        
        self.top_frame.pack()
        self.bottom_frame.pack()
        
        tkinter.mainloop()
        
    
    def textL(self):
        txt = 'левый'
        self.value.set(txt)
        
    def textR(self):
        txt = 'правый'
        self.value.set(txt)
        
    def textM(self):
        txt = 'средний'
        self.value.set(txt)
        
a = MyGui()
