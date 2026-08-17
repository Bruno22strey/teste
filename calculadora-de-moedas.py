import tkinter as tk
from tkinter import ttk, messagebox

# Janela principal
root = tk.Tk()
root.title("Conversor de Moedas")
root.geometry("500x300")
root.resizable(False, False)
root.configure(bg="#f2f2f2")


# Dicionário com a cotação de cada moeda em relação ao Real (BRL)
cotacoes = {
    "Brasil (Real)": 1.00,
    "Estados Unidos (Dólar)": 5.08,
    "Zona do Euro (Euro)": 5.90,
    "Reino Unido (Libra)": 6.80,
    "Japão (Iene)": 0.0345
}

paises = list(cotacoes.keys())


# Frame central - guarda todo o conteúdo e fica centralizado na janela
frame = tk.Frame(root, bg="#f2f2f2")
frame.place(relx=0.5, rely=0.5, anchor="center")


# Título
titulo = tk.Label(
    frame,
    text="Conversor de Moedas",
    font=("Arial", 16, "bold"),
    bg="#f2f2f2",
    fg="#070707"
)
titulo.grid(row=0, column=0, columnspan=2, pady=(0, 20))


# Campo: valor a converter
label_valor = tk.Label(frame, text="Valor:", font=("Arial", 11), bg="#f2f2f2")
label_valor.grid(row=1, column=0, sticky="e", padx=(0, 10), pady=8)

entry_valor = tk.Entry(frame, font=("Arial", 11), width=15, justify="center")
entry_valor.grid(row=1, column=1, pady=8)


# Combobox: país de origem
label_de = tk.Label(frame, text="De:", font=("Arial", 11), bg="#f2f2f2")
label_de.grid(row=2, column=0, sticky="e", padx=(0, 10), pady=8)

combo_de = ttk.Combobox(frame, font=("Arial", 10), width=22, values=paises, state="readonly", justify="center")
combo_de.grid(row=2, column=1, pady=8)
combo_de.current(0)


# Combobox: país de destino
label_para = tk.Label(frame, text="Para:", font=("Arial", 11), bg="#f2f2f2")
label_para.grid(row=3, column=0, sticky="e", padx=(0, 10), pady=8)

combo_para = ttk.Combobox(frame, font=("Arial", 10), width=22, values=paises, state="readonly", justify="center")
combo_para.grid(row=3, column=1, pady=8)
combo_para.current(1)


# Label onde aparece o resultado
label_resultado = tk.Label(
    frame,
    text="",
    font=("Arial", 12, "bold"),
    bg="#f2f2f2",
    fg="#333333"
)
label_resultado.grid(row=5, column=0, columnspan=2, pady=(15, 0))


# Função que faz a conversão
def calcular():
    try:
        valor = float(entry_valor.get())
    except ValueError:
        messagebox.showerror("Erro", "Digite um valor numérico válido.")
        return

    moeda_de = combo_de.get()
    moeda_para = combo_para.get()

    valor_em_reais = valor * cotacoes[moeda_de]
    valor_convertido = valor_em_reais / cotacoes[moeda_para]

    label_resultado.config(
        text=f"{valor:.2f} ({moeda_de}) = {valor_convertido:.2f} ({moeda_para})"
    )


# Botão calcular
botao_calcular = tk.Button(
    frame,
    text="CALCULAR",
    font=("Arial", 11, "bold"),
    bg="#1505FA",
    fg="white",
    width=15,
    height=1,
    command=calcular
)
botao_calcular.grid(row=4, column=0, columnspan=2, pady=10)


root.mainloop()