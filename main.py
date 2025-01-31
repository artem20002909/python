from tkinter import *

root = Tk()

def func1(event):
    s = ent.get()
    if s == "1234":
        lb1.configure(text="Access granted")
        lb2.destroy()
        ent.destroy()
        but = Button(root, bg="red", text="balance")
        but.bind("<Button-1>", func2)
        but.pack()
    else:
        lb1.configure(text="Wrong password. Stopped")

def func2(event):
    lb1.configure(text="Balance is 1000")

lb1 = Label(root, bg='red', text="Enter password", font="Arial 10")
lb1.grid(padx=30, pady=1)

lb2 = Label(root, text="")
lb2.grid()

ent = Entry(root, width=40, bg='yellow')
ent.grid()
ent.bind("<Return>", func1)

root.mainloop()
