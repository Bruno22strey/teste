import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("SENAI - Sistemas")
root.geometry("800x600")

checkbox_estado = tk.IntVar()


def mostrar_estado():
    if checkbox_estado.get():
        txt = "Checked"
    else:
        txt = "Unchecked"

    checkbox.config(
        text=f"Check me! ({txt})"
    )


checkbox = tk.Checkbutton(
    root,
    text="Check me! (Checked)",
    variable=checkbox_estado,
    command=mostrar_estado
)

checkbox.select()
checkbox.pack(expand=True)

root.mainloop()

#----------Conceitos-Chave-----------

#IntVar() - Variável especial do Tkinter que rastreia o estado (0 =desmarcado, 1 = marcado).

#command - Função executada automaticamente a cada mudançade estado.

#select() / deselect() - Define o estado inicial do checkbox ao carregar a janela.