from tkinter import *


def make_small(event):
    frame.configure(width=100, height=80)


def make_medium(event):
    frame.configure(width=220, height=140)


def make_large(event):
    frame.configure(width=350, height=220)


root = Tk()
root.title("Размер рамки")
root.geometry("500x400")

buttons = Frame(root)
buttons.pack(pady=15)

small = Button(buttons, text="Маленькая", width=12)
medium = Button(buttons, text="Средняя", width=12)
large = Button(buttons, text="Большая", width=12)

small.pack(side=LEFT, padx=5)
medium.pack(side=LEFT, padx=5)
large.pack(side=LEFT, padx=5)

small.bind("<Button-1>", make_small)
medium.bind("<Button-1>", make_medium)
large.bind("<Button-1>", make_large)

frame = Frame(root, width=220, height=140, bg="lightblue", bd=3, relief=GROOVE)
frame.pack(expand=True)
frame.pack_propagate(False)

root.mainloop()
