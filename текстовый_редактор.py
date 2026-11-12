from tkinter import *
from tkinter import filedialog, messagebox


def _open():
    filename = filedialog.askopenfilename(
        title="Открыть файл",
        filetypes=[("Текстовые файлы", "*.txt"), ("Все файлы", "*.*")]
    )
    if not filename:
        return

    try:
        with open(filename, "r", encoding="utf-8") as file:
            content = file.read()
    except OSError as error:
        messagebox.showerror("Ошибка", f"Не удалось открыть файл:\n{error}")
        return

    # Старый текст удаляется, чтобы новый не дописывался к нему.
    txt.delete("1.0", END)
    txt.insert(END, content)
    root.title(f"Текстовый редактор — {filename}")


def _save():
    filename = filedialog.asksaveasfilename(
        title="Сохранить файл",
        defaultextension=".txt",
        filetypes=[("Текстовые файлы", "*.txt"), ("Все файлы", "*.*")]
    )
    if not filename:
        return False

    try:
        with open(filename, "w", encoding="utf-8") as file:
            file.write(txt.get("1.0", END))
    except OSError as error:
        messagebox.showerror("Ошибка", f"Не удалось сохранить файл:\n{error}")
        return False

    root.title(f"Текстовый редактор — {filename}")
    return True


def close_win():
    save = messagebox.askyesno("Выход", "Сохранить текст перед выходом?")
    if save:
        # Если пользователь отменил сохранение, программа остается открытой.
        if _save():
            root.destroy()
    else:
        root.destroy()


def about():
    messagebox.showinfo("О программе", "Простой текстовый редактор.\n"
                                       "Учебный проект на Tkinter.")


root = Tk()
root.title("Текстовый редактор")
root.geometry("650x480")

main_menu = Menu(root)
root.config(menu=main_menu)

file_menu = Menu(main_menu, tearoff=0)
main_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Open...", command=_open)
file_menu.add_command(label="Save as...", command=_save)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=close_win)

help_menu = Menu(main_menu, tearoff=0)
main_menu.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="About program", command=about)

txt = Text(root, width=70, height=20, font="Arial 12", wrap=WORD)
txt.pack(fill=BOTH, expand=True, padx=10, pady=10)

root.protocol("WM_DELETE_WINDOW", close_win)
root.mainloop()
