from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Anti-Virus")
root.geometry("200x200")

deleted_virus = 0

def delete_virus():
    global deleted_virus
    deleted_virus = 1

def msg():
    if(deleted_virus == 0):
        messagebox.showwarning("Alert (Win32:Prank_Virus was found on your PC)", "Virus Detected! (Type:Win32:Prank_Virus)")
    else:
        messagebox.showinfo("Scan Result", "No viruses found")

lbl = Label(master=root, text="Defintely a real Anti-Virus!")
scan = Button(root, text="Scan for viruses!", command=msg)
delete = Button(root, text="Delete Viruses!", command=delete_virus)
lbl.place(x=25, y=30)
scan.place(x=50, y= 50)
delete.place(x=50, y= 75)

root.mainloop()