from tkinter import *

root = Tk()
root.title("Widgets")
root.geometry("400x600")

label1 = Label(text="Login", height=5, width=300)

label2 = Label(text="Username:", height=5, width=300)


label3 = Label(text="Password", height=5, width=300)

name = Text(height=1)
password = Text(height=1)

login = Button(text="Login")

label1.pack()
label2.pack()
name.pack()
label3.pack()
password.pack()
login.pack()

mainloop()