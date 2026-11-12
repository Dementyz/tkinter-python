from tkinter import *

root = Tk()
root.title("Форма обратной связи")
root.configure(bg="#eeeecc")
root.geometry("400x400")

Label(root, text="Ваш адрес:", font="Arial 14 bold",
      bg="#eeeecc").pack(pady=(20, 5))

address = Entry(root, width=35, font="Arial 12", bd=3)
address.pack()

Label(root, text="Комментарий:", font="Arial 14 bold",
      bg="#eeeecc").pack(pady=(10, 5))

comment = Text(root, width=38, height=9, font="Arial 11", wrap=WORD)
comment.pack()

send = Button(root, text="Отправить", width=25, height=2,
              font="Arial 13", bg="lightblue")
send.pack(pady=10)

root.mainloop()
