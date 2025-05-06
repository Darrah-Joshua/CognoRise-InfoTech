from tkinter import *
from playsound import playsound
import time
from PIL import Image, ImageTk

root = Tk()
root.title("JDFortiTech Countdown Timer")
root.geometry("400x600")
root.config(bg="#000")
root.resizable(False, False)

#JDFortiTech Logo
image_icon=PhotoImage(file="JDFortiTech Original Logo.png")
root.iconphoto(False, image_icon)

heading = Label(root, text="Countdown Timer", font="arial 30 bold", bg="#000", fg="#ea3548")
heading.pack(pady=10)

# Clock
Label(root, font=("arial", 15, "bold"), text="Current time", bg="papaya whip").place(x=65, y=70)

def clock():
    clock_time = time.strftime('%H:%M:%S %p')
    current_time.config(text=clock_time)
    current_time.place(x=190, y=70)

    # Update the clock every second
    root.after(1000, clock)  

current_time = Label(root, font=("arial", 15, "bold"), text="", fg="#000", bg="#fff")
current_time.place(x=190, y=70)
clock()

# Timer Variables
hrs = StringVar()
Entry(root, textvariable=hrs, width=2, font="arial 50", bg="#000", fg="#fff", bd=0).place(x=30, y=155)
hrs.set("00")

mins = StringVar()
Entry(root, textvariable=mins, width=2, font="arial 50", bg="#000", fg="#fff", bd=0).place(x=150, y=155)
mins.set("00")

sec = StringVar()
Entry(root, textvariable=sec, width=2, font="arial 50", bg="#000", fg="#fff", bd=0).place(x=270, y=155)
sec.set("00")

Label(root, text="hours", font="arial 12", bg="#000", fg="#fff").place(x=105, y=200)
Label(root, text="mins", font="arial 12", bg="#000", fg="#fff").place(x=225, y=200)
Label(root, text="sec", font="arial 12", bg="#000", fg="#fff").place(x=345, y=200)

# Global variable to control the timer
running = False

def update_timer():
    global running
    if running:
        times = int(hrs.get()) * 3600 + int(mins.get()) * 60 + int(sec.get())
        if times > 0:
            times -= 1

            # Convert seconds back into hours, minutes, seconds
            hour = times // 3600
            minute = (times % 3600) // 60
            second = times % 60

            # Update the displayed values
            hrs.set(f"{hour:02d}")
            mins.set(f"{minute:02d}")
            sec.set(f"{second:02d}")

            # Schedule the next update after 1 second
            root.after(1000, update_timer)
        else:
            # Timer completed
            playsound("ringtone.wav")
            running = False
            hrs.set("00")
            mins.set("00")
            sec.set("00")

def start_timer():
    global running
    
    # Prevent multiple timers from running simultaneously
    if not running:  
        running = True
        update_timer()

def stop_timer():
    global running
    running = False
    hrs.set("00")
    mins.set("00")
    sec.set("00")

def set_time():
    # Function to set the custom time range
    custom_hours = int(hrs.get())
    custom_minutes = int(mins.get())
    custom_seconds = int(sec.get())

    # Update the entry fields with the selected time
    hrs.set(f"{custom_hours:02d}")
    mins.set(f"{custom_minutes:02d}")
    sec.set(f"{custom_seconds:02d}")

def brush():
    hrs.set("00")
    mins.set("02")
    sec.set("00")

def face():
    hrs.set("00")
    mins.set("15")
    sec.set("00")

def eggs():
    hrs.set("00")
    mins.set("10")
    sec.set("00")



# Stop button
button_stop = Button(root, text="Stop", bg="#ea3548", bd=0, fg="#fff", width=20, height=2, font="arial 10 bold", command=stop_timer)
button_stop.pack(padx=5, pady=20, side=BOTTOM)

# Start button
button_start = Button(root, text="Start", bg="#ea7848", bd=0, fg="#fff", width=20, height=2, font="arial 10 bold", command=start_timer)
button_start.pack(padx=5, pady=5, side=BOTTOM)

# Set Time button
button_set = Button(root, text="Set Time", bg="#34a853", bd=0, fg="#fff", width=20, height=2, font="arial 10 bold", command=set_time)
button_set.pack(padx=5, pady=5, side=BOTTOM)



Image1 = PhotoImage(file="brush.png")
button1 = Button(root, image=Image1, bg="#000", bd=0, command=brush)
button1.place(x=7, y=270)

Image2 = PhotoImage(file="face.png")
button2 = Button(root, image=Image2, bg="#000", bd=0, command=face)
button2.place(x=137, y=270)

Image3 = PhotoImage(file="eggs.png")
button3 = Button(root, image=Image3, bg="#000", bd=0, command=eggs)
button3.place(x=267, y=270)

root.mainloop()
