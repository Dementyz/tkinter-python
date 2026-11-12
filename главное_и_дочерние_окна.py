from tkinter import *

root = Tk()
root.title("Главное окно")
root.geometry("320x170")

Label(root, text="Это главное окно", font="Arial 14").pack(pady=20)
Button(root, text="Закрыть программу", command=root.destroy).pack()

win1 = Toplevel(root, bg="lightblue", padx=15, pady=15)
win1.title("Первое дочернее окно")
win1.geometry("280x150+350+100")
Label(win1, text="Первое дочернее окно", bg="lightblue").pack(pady=10)
Button(win1, text="Закрыть окно", command=win1.destroy).pack()

win2 = Toplevel(root, bg="lightgreen", padx=15, pady=15)
win2.title("Второе дочернее окно")
win2.geometry("280x150+650+100")
Label(win2, text="Второе дочернее окно", bg="lightgreen").pack(pady=10)
Button(win2, text="Закрыть окно", command=win2.destroy).pack()

root.mainloop()
