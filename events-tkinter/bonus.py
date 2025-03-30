from tkinter import *
root = Tk()
root.title("Login App")
root.geometry("400x400")

def cancel():
    exit()

def print_out():
    print(name_entry.get(), pass_entry.get(), age_entry.get())

frame=Frame(master=root, height=200, width=360, bg="#d0efff")
lbl1 = Label(frame, text="Name: ", width=12)
lbl2 = Label(frame, text="Password: ", width=12)
lbl3 = Label(frame, text="Age: ", width=12)

name_entry = Entry(frame)
pass_entry = Entry(frame, show="*")
age_entry = Entry(frame)

btn = Button(text="Sumbit", command=print_out)
btn2 = Button(text="Cancel", command=quit)

frame.place(x=20, y=0)
lbl1.place(x=20, y=20)
name_entry.place(x=150, y=20)
lbl2.place(x=20, y=80)
pass_entry.place(x=150, y=80)
lbl3.place(x=20, y=140)
age_entry.place(x=150, y=140)
btn.place(x=130, y=210)
btn2.place(x=50, y=210)

mainloop()
