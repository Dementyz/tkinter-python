from tkinter import *


def printer(event):
    print("Как всегда очередной 'Hello World!'")


root = Tk()
root.title("Первая программа")
root.geometry("300x120")

but = Button(root, text="Печать", width=20)
but.bind("<Button-1>", printer)
but.pack(expand=True)

root.mainloop()
