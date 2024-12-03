from tkinter import *
from time import strftime

root=Tk()
root.title("clock")

def time():
    string=strftime("%H: %M: %S: %p")
    label.configure(text=string)
    label.after(1000, time)

label=Label(root, font=("ds-digital", 80),bg="black", fg="cyan")
label.pack(anchor="center")


time()
root.mainloop()



















