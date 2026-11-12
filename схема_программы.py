from tkinter import *

root = Tk()
root.title("Схема главной программы и функций")
root.resizable(False, False)

canvas = Canvas(root, width=540, height=350, bg="white",
                highlightbackground="blue", highlightthickness=5)
canvas.pack(padx=10, pady=10)

# Прямоугольники обозначают главную программу и две функции.
canvas.create_rectangle(150, 50, 175, 130, fill="lightgreen", width=2)
canvas.create_rectangle(250, 50, 275, 270, fill="yellow", width=2)
canvas.create_rectangle(375, 50, 400, 170, fill="lightblue", width=2)

# Делим главную программу на отдельные шаги.
for y in range(70, 270, 22):
    canvas.create_line(250, y, 275, y)

canvas.create_text(162, 35, text="F1", font="Arial 14 bold")
canvas.create_text(262, 35, text="P", font="Arial 14 bold")
canvas.create_text(387, 35, text="F2", font="Arial 14 bold")

# Линии со стрелками показывают вызовы функций и возврат результата.
canvas.create_line(70, 75, 145, 75, arrow=LAST, width=2)
canvas.create_line(175, 85, 210, 85, 210, 110, 247, 110,
                   arrow=LAST, width=2)
canvas.create_line(275, 150, 335, 150, 335, 80, 370, 80,
                   arrow=LAST, width=2)
canvas.create_line(247, 220, 70, 220, 70, 75, 145, 75,
                   arrow=LAST, width=2)

canvas.create_text(310, 285, text="P - main program", font="Arial 13")
canvas.create_text(310, 310, text="F1 - function 1", font="Arial 13")
canvas.create_text(310, 335, text="F2 - function 2", font="Arial 13")

root.mainloop()
