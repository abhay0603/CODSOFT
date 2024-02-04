from tkinter import *
import random

root = Tk()
root.geometry("500x500")
root.title("Password Generator")
out = StringVar()
def generator():
    password = ""
    char = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*"
    for i in range(len.get()):
        password = password + random.choice(char)
    out.set(password)

label_1=Label(root,text='Length Of Password',font='arial 12 bold').pack(pady=20)
len = IntVar()
length= Spinbox(root, from_=1, to_=32, textvariable=len,width= 25,font= "arial 16").pack()
Button(root,command=generator,text="Generate",bg='light blue',font='arial 12').pack(pady=20)
Entry(root,textvariable=out,font='arial 18').pack()
root.mainloop()