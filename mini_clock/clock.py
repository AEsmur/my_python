from tkinter import *
import tkinter.messagebox as mb


hours = 0
hours_alarm = 0
minutes = -1
minutes_alarm = 0
time1 = '00:00'
time2 = '00:00'
time_alarm = '00:00'
check = False


root = Tk()
root.title("Будильник")
root.geometry('400x200')

frame1 = Frame(root, width=300, height=150)
frame2 = Frame(root, width=300, height=30)

frame1.place(x=50, y=20)
frame2.place(x=50, y=150)

clock = Label(frame1, font='Cambria 70')
clock.config(text=time1)
clock.place(x=30, y=5)

root.resizable(width=False, height=False)


def main():
    global hours, time2, minutes

    if time_alarm == time2 and time_alarm != '00:00':
        mb.showinfo("Будильник", "Пора вставать!!!\nААААА")

    if check:
        if hours == 0 and minutes == -1:
            minutes += 1
            time2 = f"0{hours}:0{minutes}"

        elif hours < 10 and minutes < 9:
            minutes += 1
            time2 = f"0{hours}:0{minutes}"

        elif hours < 10 and minutes >= 9 and minutes < 59:
            minutes += 1
            time2 = f"0{hours}:{minutes}"


        elif hours == 23 and minutes == 59:
            minutes = 0
            hours = 0
            time2 = "00:00"

        elif hours >= 10 and hours < 23 and minutes == 59:
            minutes = 0
            hours += 1
            time2 = f"{hours}:00"
            
        elif hours < 10 and minutes == 59:
            minutes = 0
            hours += 1
            time2 = f"0{hours}:00"

        elif hours >= 10 and minutes < 9:
            minutes += 1
            time2 = f"{hours}:0{minutes}"
            
        elif hours >= 10 and minutes >= 9:
            minutes += 1
            time2 = f"{hours}:{minutes}"
            
    else:
        if hours == 0 and minutes == 0:
            minutes += 1
            time2 = f"0{hours}:0{minutes}"

        elif hours < 10 and minutes < 9:
            minutes += 1
            time2 = f"0{hours}:0{minutes}"

        elif hours < 10 and minutes >= 9 and minutes < 59:
            minutes += 1
            time2 = f"0{hours}:{minutes}"

        elif hours == 23 and minutes == 59:
            minutes = 0
            hours = 0
            time2 = "00:00"

        elif hours >= 10 and hours < 23 and minutes == 59:
            minutes = 0
            hours += 1
            time2 = f"{hours}:00"
            
        elif hours < 10 and minutes == 59:
            minutes = 0
            hours += 1
            time2 = f"0{hours}:00"

        elif hours >= 10 and minutes < 9:
            minutes += 1
            time2 = f"{hours}:0{minutes}"

        elif hours >= 10 and minutes >= 9:
            minutes += 1
            time2 = f"{hours}:{minutes}"
            
        clock.config(text=time2)
    clock.after(600, main)
    

def set_time(test):
    global hours, hours_alarm, minutes, minutes_alarm, time1, time2, time_alarm

    if check:
        if test == "hour":
            hours_alarm += 1
            
            if hours_alarm < 10 and minutes_alarm < 10:
                time_alarm = f"0{hours_alarm}:0{minutes_alarm}"

            elif hours_alarm == 24 and minutes_alarm < 10:
                hours_alarm = 0
                time_alarm = f"00:0{minutes_alarm}"                

            elif hours_alarm == 24 and minutes_alarm >= 10:
                hours_alarm = 0
                time_alarm = f"00:{minutes_alarm}"                

            elif hours_alarm >= 10 and minutes_alarm >= 10:
                time_alarm = f"{hours_alarm}:{minutes_alarm}"

            elif hours_alarm >= 10 and minutes_alarm < 10:
                time_alarm = f"{hours_alarm}:0{minutes_alarm}"

            elif hours_alarm < 10 and minutes_alarm >= 10:
                time_alarm = f"0{hours_alarm}:{minutes_alarm}"

            clock.config(text=time_alarm)

        else:
            minutes_alarm += 1
            
            if minutes_alarm < 10 and hours_alarm < 10:
                time_alarm = f"0{hours_alarm}:0{minutes_alarm}"
                
            elif minutes_alarm < 10 and hours_alarm >= 10:
                time_alarm = f"{hours_alarm}:0{minutes_alarm}"

            elif minutes_alarm == 60 and hours_alarm == 23:
                hours_alarm = 0
                minutes_alarm = 0
                time_alarm = "00:00"

            elif minutes_alarm == 60 and hours_alarm < 9:
                hours_alarm += 1
                minutes_alarm = 0
                time_alarm = f"0{hours_alarm}:00"
                
            elif minutes_alarm == 60 and hours_alarm >= 9:
                hours_alarm += 1
                minutes_alarm = 0
                time_alarm = f"{hours_alarm}:00"
                
            elif minutes_alarm >= 10 and hours_alarm < 10:
                time_alarm = f"0{hours_alarm}:{minutes_alarm}"

            elif minutes_alarm >= 10 and hours_alarm >= 10:
                time_alarm = f"{hours_alarm}:{minutes_alarm}"

            clock.config(text=time_alarm)
    else:
        if test == "hour":
            hours += 1
            
            if hours < 10 and minutes < 10:
                time1 = f"0{hours}:0{minutes}"                
                
            elif hours == 24 and minutes < 10:
                hours = 0
                time1 = f"00:0{minutes}"
                
            elif hours == 24 and minutes >= 10:
                hours = 0
                time1 = f"00:{minutes}"

            elif hours >= 10 and minutes >= 10:
                time1 = f"{hours}:{minutes}"

            elif hours >= 10 and minutes < 10:
                time1 = f"{hours}:0{minutes}"

            elif hours < 10 and minutes >= 10:
                time1 = f"0{hours}:{minutes}"
                
            time2 = time1
            clock.config(text=time2)

        else:
            minutes += 1
            
            if minutes < 10 and hours < 10:
                time1 = f"0{hours}:0{minutes}"
                
            elif minutes < 10 and hours >= 10:
                time1 = f"{hours}:0{minutes}"

            elif minutes == 60 and hours == 23:
                hours = 0
                minutes = 0
                time1 = "00:00"

            elif minutes == 60 and hours < 9:
                hours += 1
                minutes = 0
                time1 = f"0{hours}:00"                

            elif minutes == 60 and hours >= 9:
                hours += 1
                minutes = 0
                time1 = f"{hours}:00"

            elif minutes >= 10 and hours < 10:
                time1 = f"0{hours}:{minutes}"

            elif minutes >= 10 and hours >= 10:
                time1 = f"{hours}:{minutes}"

            time2 = time1
            clock.config(text=time2)


def set_alarm():
    global check, time_alarm
    
    if not check and time_alarm == '00:00':
        check = True
        clock.config(text=time_alarm)
        
    elif not check and time_alarm != '00:00':
        check = False
        time_alarm = '00:00'
        clock.config(text=time2)
        
    else:
        check = False
        clock.config(text=time2)


def set_hours():
    set_time("hour")

def set_minutes():
    set_time("minute")


buttonH = Button(frame2, text="H",
                 font='Cambria 11', width=5, command=set_hours)
buttonH.place(x=40, y=0)

buttonM = Button(frame2, text="M",
                 font='Cambria 11', width=5, command=set_minutes)
buttonM.place(x=120, y=0)

buttonA = Button(frame2, text="A",
                 font='Cambria 11', width=5, command=set_alarm)
buttonA.place(x=200, y=0)


main()
root.mainloop()
