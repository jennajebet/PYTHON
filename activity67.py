from tkinter import*

root=Tk()
root.title("Login app")
root.geometry("400x400")

frame=Frame(master=root, width=300, height=300, bg="lightgrey")

lbl1=Label(frame, text="Fullname", bg="lightblue", fg="white", width=12)
lbl2=Label(frame, text="Password", bg="lightblue", fg="white", width=12)
lbl3=Label(frame, text="Email ID", bg="lightblue", fg="white", width=12)

name_entry=Entry(frame)
email_entry=Entry(frame)
password_entry=Entry(frame, show="*")

def display():
    name=name_entry.get()
    greet="Hey"+ " "+name
    message="\nCongratulations on your new account!!"
    textbox.insert(END, greet)
    textbox.insert(END, message)


