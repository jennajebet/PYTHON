from tkinter import *
from datetime import date

root=Tk()

root.title("tk widgits")

root.geometry("500x400")

lbl= Label(text="Suit and tie", fg="white", bg="orange", height=1, width=500)

name_lbl= Label(text="Full name", fg="blue", bg="purple")

name=Entry()

root.mainloop()