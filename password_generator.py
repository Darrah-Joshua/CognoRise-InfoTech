from tkinter import*
from random import randint
from PIL import Image, ImageTk

root = Tk()
root.title('Password Generator')
root.geometry("500x300")
# root.configure(bg="lightblue")


#JDFortiTech Logo
image_icon=PhotoImage(file="JDFortiTech Original Logo.png")
root.iconphoto(False, image_icon)


#Generating random strong password
def new_rand():
    # Clearing Our Entry Box
    pw_entry.delete(0, END)

    # Getting PW Length
    pw_length = int(my_entry.get())

    # Creating a variable to hold our password
    my_password = ''

    # Looping through password length
    for x in range(pw_length):
        my_password += chr(randint(33, 126))
    
    # Outputing password to the screen
    pw_entry.insert(0, my_password)


#Copying to clipboard
def clipper():
    #Clearing clipboard
    root.clipboard_clear()
    #Copying to clipboard
    root.clipboard_append(pw_entry.get())

#Labelling Frame
lf = LabelFrame(root, text = "How Many Characters?")
lf.pack(pady = 20)

#creating Entry Box To Designate Number of Character
my_entry = Entry(lf, font = ("Helvetica", 24))
my_entry.pack(pady = 20)


#creating Entry Box For Our Returned Password
pw_entry = Entry(root, text='', font = ("Helvetica", 24), bd=0, bg="systembuttonface")
pw_entry.pack(pady = 20)


#Creating a frame for our Buttons
my_frame =  Frame(root)
my_frame.pack(pady=20)

#Creating our Buttons
my_button = Button(my_frame, text= "Generate Strong Password", command=new_rand)
my_button.grid(row=0, column=0, padx=10)

clip_button = Button(my_frame, text="Copy To Clipboard", command=clipper)
clip_button.grid(row=0, column=1, padx=10)

root.mainloop()