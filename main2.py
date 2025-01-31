from tkinter import *
root = Tk()
cnv = Canvas(root, width=300, height=280)
cnv.pack()
root.title("tags")

def func1(en):
    cnv.move(kolo, 0, 40)
    
def func2(en):
    cnv.itemconfig(kvadrat, fill="red", width=5)

kvadrat=cnv.create_rectangle(20, 10, 70, 60, fill="cyan",
                             outline="blue")

kolo=cnv.create_oval([160, 10], [210, 60], fill="yellow")

but1 = Button(root)
but1["text"] = "kolo"
but1.bind("<Button-1>", func2)

but2 = Button(root)
but2["text"] = "kvadrat color"
but2.bind("<Button-1>", func1)

but1.pack()
but2.pack()
root.mainloop()

