from tkinter import *

root = Tk()
root.title("Шкала и текстовое поле")
root.geometry("550x300")
root.configure(bg="#eeeecc")

top = Frame(root, width=550, height=170, bg="#00ee00")
top.pack(fill=X)
top.pack_propagate(False)

scale = Scale(top, from_=0, to=100, orient=HORIZONTAL,
              length=480, tickinterval=10, resolution=1)
scale.pack(padx=25, pady=35)

bottom = Frame(root, width=240, height=130, bg="darkgreen")
bottom.pack(pady=0)
bottom.pack_propagate(False)

entry = Entry(bottom, width=20, font="Arial 12")
entry.pack(expand=True)

root.mainloop()
