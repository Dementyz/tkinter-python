from tkinter import *


def move_down(event):
    canvas.move(rect, 0, 2)


def clean(event):
    canvas.delete(ALL)


root = Tk()
root.title("Идентификаторы объектов")

canvas = Canvas(root, width=460, height=460, bg="grey80")
canvas.pack()

oval = canvas.create_oval(30, 10, 130, 80, fill="white")
rect = canvas.create_rectangle(180, 10, 280, 80, fill="lightgreen")
trian = canvas.create_polygon(330, 80, 380, 10, 430, 80,
                              fill="grey80", outline="black")

# Методы move, itemconfig и coords изменяют уже созданные объекты.
canvas.move(rect, 0, 150)
canvas.itemconfig(trian, outline="red", width=3)
canvas.coords(oval, 300, 200, 450, 450)

# Каждый щелчок по прямоугольнику опускает его еще на два пикселя.
canvas.tag_bind(rect, "<Button-1>", move_down)
canvas.bind("<Delete>", clean)
canvas.focus_set()

root.mainloop()
