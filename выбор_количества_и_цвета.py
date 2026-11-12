from tkinter import *

root = Tk()
root.title("Выбор параметров")
root.configure(bg="#eeeecc")
root.geometry("280x470")

Label(root, text="Сколько штук?", font="Arial 13",
      bg="#eeeecc").pack(pady=(20, 10))

amount = IntVar()
amount.set(0)

for text, value in [("0-10", 0), ("11-20", 1),
                    ("21-30", 2), ("31-40", 3)]:
    Radiobutton(root, text=text, variable=amount, value=value,
                font="Arial 12", bg="#eeeecc",
                activebackground="#eeeecc").pack(anchor="w", padx=70, pady=5)

Label(root, text="Какого цвета?", font="Arial 13",
      bg="#eeeecc").pack(pady=(20, 10))

colors = [("RED", "red"), ("BLUE", "blue"),
          ("GREEN", "green"), ("YELLOW", "yellow")]
color_vars = []

for text, color in colors:
    var = IntVar()
    color_vars.append(var)
    Checkbutton(root, text=text, variable=var, onvalue=1, offvalue=0,
                width=10, anchor="w", bg=color,
                activebackground=color).pack(pady=2)

root.mainloop()
