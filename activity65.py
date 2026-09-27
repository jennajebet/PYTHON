from tkinter import *
from datetime import date

root=Tk()

root.title("tk widgits")

root.geometry("500x400")

lbl= Label(text="Suit and tie", fg="white", bg="orange", height=1, width=500)

name_lbl= Label(text="Full name", fg="blue", bg="purple")

name_entry=Entry()

def display():
    name= name_entry.get()

    global message

    message="welcome to the application! \nTodays date is:"

    greet= "hello!"+name+ "\n"

    text_box.insert(END, greet)
    text_box.insert(END, message)
    text_box.insert(END, date.today())

text_box= Text(height=3)

btn= Button(text="press me!", command= display, height=1, bg= "pink", fg="black")

lbl.pack()
name_lbl.pack()
name_entry.pack()
btn.pack()
text_box.pack()

root.mainloop()