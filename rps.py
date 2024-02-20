from tkinter import *
import random

root = Tk()
root.geometry("400x400")
root.title("Rock,Paper,Scissors Game")


blank_img = PhotoImage(file="blank.png")
blank_1 = blank_img.subsample(1, 1)
user_rock = PhotoImage(file="rock.jpeg")
photo_image_1 = user_rock.subsample(1, 1)
user_paper = PhotoImage(file="paper.png")
photo_image_2 = user_paper.subsample(1, 1)
user_scissors = PhotoImage(file="scissors.png")
photo_image_3 = user_scissors.subsample(1, 1)
machine_rock = PhotoImage(file="rock.jpeg")
machine_paper = PhotoImage(file="paper.png")
machine_scissors = PhotoImage(file="scissors.png")


def rock():
    global user_option
    user_option = 1
    result()


def paper():
    global user_option
    user_option = 2
    result()


def scissors():
    global user_option
    user_option = 3
    result()


def machine_rock():
    if user_option == 1:
        Label_Status.config(text="Game Tie")
    elif user_option == 2:
        Label_Status.config(text="You Won")
    elif user_option == 3:
        Label_Status.config(text="You Lose")


def machine_paper():
    if user_option == 1:
        Label_Status.config(text="You Win")
    elif user_option == 2:
        Label_Status.config(text="Game Tie")
    elif user_option == 3:
        Label_Status.config(text="You Lose")


def machine_scissors():
    if user_option == 1:
        Label_Status.config(text="You Win")
    elif user_option == 2:
        Label_Status.config(text="You Lose")
    elif user_option == 3:
        Label_Status.config(text="Game Tie")


def result():
    machine_option = random.randint(1, 3)
    if machine_option == 1:
        Image_machine.configure(image=photo_image_1)
        machine_rock()
    elif machine_option == 2:
        Image_machine.configure(image=photo_image_2)
        machine_paper()
    elif machine_option == 3:
        Image_machine.configure(image=photo_image_3)
        machine_scissors()


Label(root, text='Rock Paper Scissors', font='arial 12 bold').grid(row=1, column=1, columnspan=3, padx=10, pady=10)
Image_machine = Label(root, image=blank_1)
Image_machine.grid(row=2, column=1, columnspan=3, padx=10, pady=10)
Label_Status = Label(root, text="", font=('Times New Roman', 12))
Label_Status.config(fg="black", font=('Times New Roman', 20, 'bold', 'italic'))
Label_Status.grid(row=3, column=1, columnspan=3, padx=10, pady=10)
Button(root, image=photo_image_1, command=rock).grid(row=4, column=1, padx=10, pady=10)
Button(root, image=photo_image_2, command=paper).grid(row=4, column=2, padx=10, pady=10)
Button(root, image=photo_image_3, command=scissors).grid(row=4, column=3, padx=10, pady=10)


root.mainloop()
