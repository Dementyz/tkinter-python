from tkinter import *


def set_color(color):
    frame.configure(bg=color)


def set_size(width, height):
    frame.configure(width=width, height=height)


root = Tk()
root.title("Меню: цвет и размер")
root.geometry("760x580")

frame = Frame(root, width=300, height=150, bg="black")
frame.pack(padx=20, pady=20)
frame.pack_propagate(False)

main_menu = Menu(root)
root.config(menu=main_menu)

color_menu = Menu(main_menu, tearoff=0)
main_menu.add_cascade(label="Color", menu=color_menu)
color_menu.add_command(label="Red", command=lambda: set_color("red"))
color_menu.add_command(label="Green", command=lambda: set_color("green"))
color_menu.add_command(label="Blue", command=lambda: set_color("blue"))

size_menu = Menu(main_menu, tearoff=0)
main_menu.add_cascade(label="Size", menu=size_menu)
size_menu.add_command(label="500x500", command=lambda: set_size(500, 500))
size_menu.add_command(label="700x400", command=lambda: set_size(700, 400))

root.mainloop()
