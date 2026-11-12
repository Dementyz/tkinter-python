from tkinter import *


def color(event):
    # Изменятся сразу оба объекта с тегом group1.
    canvas.itemconfig("group1", fill="red", width=3)


def clean(event):
    canvas.delete(ALL)


root = Tk()
root.title("Теги объектов Canvas")

canvas = Canvas(root, width=460, height=180, bg="grey80")
canvas.pack()

oval = canvas.create_oval(30, 10, 130, 80, tag="group1", fill="orange")
canvas.create_line(10, 100, 450, 100, tag="group1")

Label(root, text="Правая кнопка мыши — изменить цвет, Delete — очистить").pack(pady=8)

canvas.bind("<Button-3>", color)
canvas.bind("<Delete>", clean)
canvas.focus_set()

root.mainloop()
