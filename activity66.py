from tkinter import*

root=Tk()

root.title("Number pad")

root.geometry("500x400")

frame=Frame(master=root, height=300, width=250, bg="darkgray")

num=[[9,8,7],
     [6,5,4],
     [3,2,1],
     ['#', 0, '*']]
