from tkinter import *
from tkinter import ttk

root = Tk()
root.title("my list")

frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="good morning").grid(column=10, row=15)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=10, row=15)
root.mainloop()
  

