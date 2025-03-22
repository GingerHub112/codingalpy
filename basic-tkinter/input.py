from tkinter import *
from datetime import date

root = Tk()
root.title("Widgets")
root.geometry("400x600")

label = Label(text="Hey, There!", fg="white", bg="#072F5F", height=1, width=300)

name_label = Label(text="Full Name", bg="#3895D3")
name_entry = Entry()

def display():
    name = name_entry.get()

    global message
    message = "Welcome to my program!\nToday's date is: "
    greet = "Hello "+name+"\n"

    text_box.insert(END, greet)
    text_box.insert(END, message)
    text_box.insert(END, date.today())

text_box = Text(height=1)
btn = Button(text="Begin", command=display, height=1, bg="#1261A0", fg="white")

label.pack()
name_label.pack()
name_entry.pack()
btn.pack()
text_box.pack()

mainloop()