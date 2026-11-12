from tkinter import *


def erase():
    # Удаляем третью строку вместе с символом перехода на новую строку.
    tx.delete("3.0", "4.0")


def smiley(event):
    cv = Canvas(tx, height=30, width=30, highlightthickness=0)
    cv.create_oval(1, 1, 29, 29, fill="yellow")
    cv.create_oval(9, 10, 12, 12)
    cv.create_oval(19, 10, 22, 12)
    cv.create_polygon(9, 20, 15, 24, 22, 20)
    tx.window_create(CURRENT, window=cv)
    smileys.append(cv)
    return "break"


root = Tk()
root.title("Возможности виджета Text")

tx = Text(root, font=("times", 13), width=62, height=20, wrap=WORD)
tx.pack(padx=10, pady=10)

text = ('Дзен Питона\n'
        'Если интерпретатору Питона дать команду\n'
        'import this ("импортировать это"),\n'
        'то выведется так называемый "Дзен Питона".\n'
        'Некоторые выражения:\n'
        '* Если реализацию сложно объяснить — это плохая идея.\n'
        '* Ошибки никогда не должны замалчиваться.\n'
        '* Явное лучше неявного.\n')
tx.insert("1.0", text)

# Третий тег задает шрифт остальной части текста.
tx.tag_add("other", "2.0", END)
tx.tag_add("title", "1.0", "1.end")
tx.tag_add("special", "6.0", "8.end")
tx.tag_add("special", "3.0", "3.11")

tx.tag_config("other", font=("courier", 12))
tx.tag_config("title", foreground="red",
              font=("times", 16, "underline"), justify=CENTER)
tx.tag_config("special", background="lightgray",
              font=("courier", 12, "bold"))

smileys = []
tx.bind("<Button-1>", smiley)

# Кнопка из примера вставляется прямо в текстовое поле.
tx.insert(END, "\n")
erase_button = Button(tx, text="Стереть третью строку", command=erase)
tx.window_create(END, window=erase_button)

# Дополнительный виджет — обычное однострочное поле ввода.
tx.insert(END, "\n")
extra_entry = Entry(tx, width=35, font="Arial 11")
extra_entry.insert(0, "Дополнительное поле ввода")
tx.window_create(END, window=extra_entry)

root.mainloop()
