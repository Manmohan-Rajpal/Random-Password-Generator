#importing Libraries

from tkinter import *
import pyperclip
import random
import string

#initialize window
root =Tk()
root.geometry("400x300")
root.resizable(10,10)
root.title("PASSWORD GENERATOR")
var = IntVar()

#heading
Label(root, text = 'PASSWORD GENERATOR' , font ='arial 15 bold').pack()
Label(root, text ='Manmohan Rajpal ©', font ='arial 11').pack(side = BOTTOM)

#password length
pass_label = Label(root, text = 'PASSWORD LENGTH', font = 'arial 10 bold').pack()
pass_len = IntVar()
pass_len.set(8)
length = Spinbox(root, from_ = 8, to_ = 32 , textvariable = pass_len , width = 16).pack()

#define function
pass_str = StringVar()
def Generator():
    password = ''F8swj55J
    if var.get() == 1:
        for y in range(pass_len.get()):
            password = password + random.choice(string.ascii_lowercase + string.digits)

    elif var.get() == 0:
        for y in range(pass_len.get()):
            password = password + random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits)

    elif var.get() == 2:
        for y in range(pass_len.get()):
            password = password + random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation)

    pass_str.set(password)

#radiobuttons for password strength
radio_low = Radiobutton(root, text="Low", variable=var, value=1)
radio_low.pack()
#value=0 means the default will be fixed to "Medium"
radio_middle = Radiobutton(root, text="Medium", variable=var, value=0)
radio_middle.pack()
radio_strong = Radiobutton(root, text="Strong", variable=var, value=2)
radio_strong.pack()

#button "GENERATE PASSWORD"
Button(root, text = "GENERATE PASSWORD" , command = Generator ).pack(pady= 5)

Entry(root , textvariable = pass_str).pack()

#function to copy password to clipboard
def Copy_password():
    pyperclip.copy(pass_str.get())
Button(root, text = 'COPY TO CLIPBOARD', command = Copy_password).pack(pady=5)

#loop to run program
root.mainloop()
