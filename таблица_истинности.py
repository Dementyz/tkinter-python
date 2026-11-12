from tkinter import *

root = Tk()
root.title("Таблица истинности")
root.resizable(False, False)

canvas = Canvas(root, width=420, height=250, bg="white", highlightthickness=2)
canvas.pack(padx=10, pady=10)

headers = ["X", "Y", "X and Y", "X or Y"]
rows = [
    ["0", "0", "0", "0"],
    ["0", "1", "0", "1"],
    ["1", "0", "0", "1"],
    ["1", "1", "1", "1"]
]

x_lines = [0, 100, 210, 320, 420]
y_lines = [0, 50, 100, 150, 200, 250]

for x in x_lines:
    canvas.create_line(x, 0, x, 250, width=2)
for y in y_lines:
    canvas.create_line(0, y, 420, y, width=2)

for column, header in enumerate(headers):
    x = (x_lines[column] + x_lines[column + 1]) // 2
    canvas.create_text(x, 25, text=header, font="Arial 15")

for row, values in enumerate(rows):
    y = 75 + row * 50
    for column, value in enumerate(values):
        x = (x_lines[column] + x_lines[column + 1]) // 2
        canvas.create_text(x, y, text=value, font="Arial 18 bold")

root.mainloop()
