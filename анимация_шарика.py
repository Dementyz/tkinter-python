from tkinter import *


def move_ball():
    global dx, animation

    x1, y1, x2, y2 = canvas.coords(ball)
    if x2 >= 450 and dx > 0:
        dx = -dx
    elif x1 <= 10 and dx < 0:
        dx = -dx

    canvas.move(ball, dx, 0)
    animation = root.after(20, move_ball)


def start():
    global animation
    if animation is None:
        move_ball()


def stop():
    global animation
    if animation is not None:
        root.after_cancel(animation)
        animation = None


def close():
    stop()
    root.destroy()


root = Tk()
root.title("Движение шарика")
root.resizable(False, False)

canvas = Canvas(root, width=460, height=250, bg="lightblue")
canvas.pack()

ball = canvas.create_oval(20, 90, 70, 140, fill="orange", outline="darkred", width=2)
dx = 3
animation = None

buttons = Frame(root)
buttons.pack(pady=10)
Button(buttons, text="Старт", width=10, command=start).pack(side=LEFT, padx=5)
Button(buttons, text="Стоп", width=10, command=stop).pack(side=LEFT, padx=5)

start()
root.protocol("WM_DELETE_WINDOW", close)
root.mainloop()
