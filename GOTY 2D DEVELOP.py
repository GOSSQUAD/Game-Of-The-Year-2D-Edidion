from tkinter import *

root=Tk()
root.geometry("1366x768")
rootimg=PhotoImage(file="root.gif")

l = Label(image = rootimg)
l.pack()

root.mainloop()