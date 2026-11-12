from tkinter import *

root = Tk()
root.title("Текстовое поле")
root.geometry("520x180")

text = Text(root, width=48, height=5, font="Arial 12", wrap=WORD)
scroll = Scrollbar(root, command=text.yview)
text.configure(yscrollcommand=scroll.set)

text.pack(side=LEFT, fill=BOTH, expand=True, padx=(10, 0), pady=10)
scroll.pack(side=RIGHT, fill=Y, padx=(0, 10), pady=10)

text.insert(END, "Это многострочное текстовое поле с движком и "
                 "вертикальной полосой прокрутки. Если сюда ввести много "
                 "текста, то его можно будет прокручивать.\n" * 4)

root.mainloop()
