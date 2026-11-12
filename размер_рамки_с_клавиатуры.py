from tkinter import *


def change_size(event):
    try:
        width = int(width_entry.get())
        height = int(height_entry.get())
        if width <= 0 or height <= 0:
            raise ValueError
    except ValueError:
        message.configure(text="Введите положительные целые числа")
        return

    frame.configure(width=width, height=height)
    message.configure(text=f"Размер рамки: {width} x {height}")


root = Tk()
root.title("Изменение размера рамки")
root.geometry("650x450")

controls = Frame(root)
controls.pack(pady=15)

Label(controls, text="Ширина:").grid(row=0, column=0, padx=5)
width_entry = Entry(controls, width=8)
width_entry.grid(row=0, column=1, padx=5)
width_entry.insert(END, "250")

Label(controls, text="Высота:").grid(row=0, column=2, padx=5)
height_entry = Entry(controls, width=8)
height_entry.grid(row=0, column=3, padx=5)
height_entry.insert(END, "150")

Label(root, text="После ввода чисел нажмите пробел").pack()

frame = Frame(root, width=250, height=150, bg="lightgreen", bd=3, relief=SUNKEN)
frame.pack(expand=True)
frame.pack_propagate(False)

message = Label(root, text="Размер рамки: 250 x 150")
message.pack(pady=10)

root.bind("<space>", change_size)
root.mainloop()
