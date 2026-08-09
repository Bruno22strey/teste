import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("SENAI - Sistemas")
root.geometry("800x600")


def selecao_mudou(evento):
        label.config(text=f"{evento.widget.get()}selecionado!")

combobox = ttk.Combobox(root, values=["Primeiro", "Segundo", "Terceiro"])

combobox.set("Primeiro")

combobox.bind("<<ComboboxSelected>>", selecao_mudou)

combobox.pack()

label = tk.Label(root, text="Primeiro selecionado!")
label.pack()

root.mainloop()

#values - Lista de opções disponíveis para o usuário selecionar.

#set() - Define o valor exibido inicialmente no campo.

#bind() - Associa o evento <<ComboboxSelected>> a uma função de callback. Disparado quando se seleciona um item.