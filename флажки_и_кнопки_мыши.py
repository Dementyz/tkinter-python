from tkinter import *


def show_checked(event):
    lines = []
    for name, var in flags:
        if var.get() == 1:
            lines.append(name + " = 1")

    if not lines:
        lines = ["Нет включенных флажков"]

    text.delete("1.0", END)
    text.insert(END, "Включенные флажки:\n" + "\n".join(lines))
    return "break"


def show_unchecked(event):
    lines = []
    for name, var in flags:
        if var.get() == 0:
            lines.append(name + " = 0")

    if not lines:
        lines = ["Нет выключенных флажков"]

    text.delete("1.0", END)
    text.insert(END, "Выключенные флажки:\n" + "\n".join(lines))
    return "break"


root = Tk()
root.title("Состояние флажков")
root.geometry("430x330")

Label(root, text="Левый щелчок — включенные, правый — выключенные").pack(pady=10)

flags = []
for name in ["Окружность", "Квадрат", "Треугольник"]:
    var = IntVar()
    Checkbutton(root, text=name, variable=var, onvalue=1, offvalue=0,
                anchor="w", width=25).pack(padx=30, pady=2)
    flags.append((name, var))

text = Text(root, width=42, height=9, font="Arial 11")
text.pack(pady=15)
text.insert(END, "Щелкните в этом поле левой или правой кнопкой мыши.")
text.bind("<Button-1>", show_checked)
text.bind("<Button-3>", show_unchecked)

root.mainloop()
