from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename

window = Tk()
window.title()
window.title("Text Editor")
window.geometry("600x500")
window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=300, weight=1)

font_options = ["Times New Roman", "Arial", "Comic Sans MS"]

selected_option = StringVar()
selected_option.set(font_options[0])

def open_file():
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All files", "*.*")]
    )
    print(filepath)
    if not filepath:
        return
    txt_edit.delete(1.0, END)

    with open(filepath, "r", encoding="utf-8") as input_file:
        text = input_file.read()
        txt_edit.insert(END, text)
        input_file.close()
    window.title(f"Text Editor - {filepath}")

def save_file():
    filepath = asksaveasfilename(
        defaultextension="txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
    )
    if not filepath:
        return
    with open(filepath, "w") as output_file:
        text = txt_edit.get(1.0, END)
        output_file.write(text)
    window.title(f"Text Editor - {filepath}")

def update_font(*args):
    txt_edit.config(font=(selected_option.get(), 12))

txt_edit = Text(window, font=(selected_option.get(), 12))
fr_buttons = Frame(window, relief=RAISED, bd=2)
btn_open = Button(fr_buttons, text="Open", command=open_file)
btn_save = Button(fr_buttons, text="Save As...", command=save_file)
dropdown = OptionMenu(fr_buttons, selected_option, *font_options)

btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_save.grid(row=1, column=0, sticky="ew", padx=5)
dropdown.grid(row=2, column=0, sticky="ew", padx=5, pady=5)

fr_buttons.grid(row=0, column=0, sticky="ns")
txt_edit.grid(row=0, column=1, sticky="nsew")

selected_option.trace_add("write", update_font)

window.mainloop()
