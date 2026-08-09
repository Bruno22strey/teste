import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("SENAI - Sistemas")
root.geometry("800x600")

#StringVar é uma variável que armazena uma string
# é usada para atualizar widget dinamicamente
spinbox_var = tk.StringVar(value="0")

spinbox = tk.Spinbox(root,
    from_=-10,
    to=10,
    # increment=5,
    textvariable=spinbox_var)

spinbox.pack(expand=True)

label = tk.Label(root, textvariable=spinbox_var)
label.pack()

root.mainloop()

#-----------Parâmetros Principais----------

#from_ / to - Define o intervalo mínimo e máximo de valores permitidos.

#textvariable - Vincula uma StringVar para ler ou atualizar o valor programaticamente.

#values - Alternativa: lista fixa de opções em vez de intervalo numérico.