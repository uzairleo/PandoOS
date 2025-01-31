from tkinter import *
from tkinter.ttk import *
import subprocess as sp
import tkinter.messagebox as mb
import os
import random

root = Tk()
root.title("Welcome To PandoOS")
root.geometry("300x100")
root.iconbitmap("img/logo.ico")
root.bind("<Escape>", lambda e: root.destroy())
root.resizable(False, False)
root.withdraw()

version = '4.0'

# Boot (start)

def boot():
    os.system('cls')
    mb.showinfo("PandoOS","Boot successful, press ENTER for continue.")
    # root.destroy()
    os.system('cls')
    print("PandoOS> Boot...")
    print(f"PandoOS> Latest version: {version}")
    pandoos = "PandoOS.py"
    os.system(pandoos)

boot()

# UI

# Label(root, text="\n").pack()
# boot = Button(root, text="Boot PandoOS", command=boot, width=30)
# boot.pack(anchor='center')
# boot.grid()

# root.mainloop()
