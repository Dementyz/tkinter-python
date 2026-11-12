from tkinter import *


def show_text(event):
    label.configure(text=entry.get())


root = Tk()
root.title("Ввод текста")
root.geometry("450x170")

Label(root, text="Введите текст и нажмите Enter:").pack(pady=(20, 5))

entry = Entry(root, width=45, font="Arial 12")
entry.pack(pady=5)
entry.bind("<Return>", show_text)

label = Label(root, text="Здесь появится ваш текст",
              font="Arial 13", fg="darkblue", wraplength=400)
label.pack(pady=20)

entry.focus_set()
root.mainloop()
