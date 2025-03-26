from tkinter import *
root = Tk()
root.title("Login App")
root.geometry("400x400")

frame=Frame(master=root, height=200, width=360, bg="#d0efff")
lbl1 = Label(frame, text="Full Name: ", bg="#3895D3", fg="white", width=12)
lbl2 = Label(frame, text="Email: ", bg="#3895D3", fg="white", width=12)
lbl3 = Label(frame, text="Password: ", bg="#3895D3", fg="white", width=12)

name_entry = Entry(frame)
email_entry = Entry(frame)
password_entry = Entry(frame, show="*")

def display():
    textbox.config(state="normal")
    name = name_entry.get()
    greet = "Hey " + name + "\n"
    message = "Congratulations on your new account!"
    textbox.insert(END, greet)
    textbox.insert(END, message)
    textbox.config(state="disabled")

textbox = Text(bg="#BEBEBE", fg="black")
btn = Button(text="Create Account", command=display, bg="red")

frame.place(x=20, y=0)
lbl1.place(x=20, y=20)
name_entry.place(x=150, y=20)
lbl2.place(x=20, y=80)
email_entry.place(x=150, y=80)
lbl3.place(x=20, y=140)
password_entry.place(x=150, y=140)
btn.place(x=130, y=210)
textbox.place(y=250)

textbox.config(state="disabled")
mainloop()