from tkinter import *


def change_color(value):
    number = int(float(value))
    frame.configure(bg=colors[number])
    color_name.configure(text=names[number])


root = Tk()
root.title("Выбор цвета")
root.geometry("420x330")

frame = Frame(root, width=300, height=140, bg="red", bd=3, relief=RIDGE)
frame.pack(pady=20)
frame.pack_propagate(False)

colors = ["red", "green", "blue", "yellow", "purple"]
names = ["Красный", "Зеленый", "Синий", "Желтый", "Фиолетовый"]

scale = Scale(root, from_=0, to=4, orient=HORIZONTAL, length=300,
              tickinterval=1, resolution=1, command=change_color,
              label="0 — красный, 1 — зеленый, 2 — синий, 3 — желтый, 4 — фиолетовый")
scale.pack(padx=20)

color_name = Label(root, text="Красный", font="Arial 13")
color_name.pack(pady=10)

root.mainloop()
