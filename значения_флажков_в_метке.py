from tkinter import *


def show_values():
    values = var0.get() + ", " + var1.get() + ", " + var2.get()
    result.configure(text=values)


root = Tk()
root.title("Переменные Tkinter")
root.geometry("350x280")

var0 = StringVar()
var1 = StringVar()
var2 = StringVar()

ch0 = Checkbutton(root, text="Окружность", variable=var0,
                  onvalue="circle", offvalue="-")
ch1 = Checkbutton(root, text="Квадрат", variable=var1,
                  onvalue="square", offvalue="-")
ch2 = Checkbutton(root, text="Треугольник", variable=var2,
                  onvalue="triangle", offvalue="-")

for check in [ch0, ch1, ch2]:
    check.deselect()
    check.pack(anchor="w", padx=40, pady=5)

Button(root, text="Получить значения", command=show_values).pack(pady=15)

result = Label(root, text="-, -, -", font="Arial 13", fg="darkblue")
result.pack(pady=10)

root.mainloop()
