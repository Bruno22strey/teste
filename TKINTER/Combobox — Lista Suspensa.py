import tkinter as tk
from tkinter import ttk, messagebox

# Janela principal
root = tk.Tk()
root.title("Tela de Cadastro")
root.geometry("450x500")
root.resizable(False, False)
root.configure(bg="#f2f2f2")


# Título
titulo = tk.Label(
    root,
    text="SENAI - Cadastro",
    font=("Arial", 18, "bold"),
    bg="#f2f2f2",
    fg="#2ee700"
)
titulo.grid(row=0, column=0, columnspan=2, pady=(20, 10))


# Foto de perfil
try:
    imagem = tk.PhotoImage(file="logo.png")
    imagem = imagem.subsample(3, 3)

    label_imagem = tk.Label(root, image=imagem, bg="#f2f2f2")
    label_imagem.image = imagem  # evita a imagem sumir
    label_imagem.grid(row=1, column=0, columnspan=2, pady=10)

except Exception:
    label_imagem = tk.Label(
        root,
        text="👤\nFoto de perfil",
        font=("Arial", 24),
        bg="#dddddd",
        width=12,
        height=4
    )
    label_imagem.grid(row=1, column=0, columnspan=2, pady=10)


# Função auxiliar para criar campo de texto (label + entry lado a lado)
def criar_campo(linha, coluna, texto):
    label = tk.Label(root, text=texto, font=("Arial", 10), bg="#f2f2f2")
    label.grid(row=linha, column=coluna, sticky="w", padx=(20, 5), pady=(10, 0))

    entry = tk.Entry(root, font=("Arial", 11), width=16)
    entry.grid(row=linha + 1, column=coluna, padx=(20, 5), pady=(0, 5))
    return entry


# Função auxiliar para criar combobox (label + combobox lado a lado)
def criar_combobox(linha, coluna, texto, opcoes):
    label = tk.Label(root, text=texto, font=("Arial", 10), bg="#f2f2f2")
    label.grid(row=linha, column=coluna, sticky="w", padx=(20, 5), pady=(10, 0))

    combo = ttk.Combobox(root, font=("Arial", 11), width=14, values=opcoes, state="readonly")
    combo.grid(row=linha + 1, column=coluna, padx=(20, 5), pady=(0, 5))
    return combo


# Linha 2/3: Nome e Idade
entry_nome = criar_campo(2, 0, "Nome:")
entry_idade = criar_campo(2, 1, "Idade:")

# Linha 4/5: Cor dos olhos (combobox) e Sexo (combobox)
combo_olhos = criar_combobox(4, 0, "Cor dos olhos:", ["Castanho", "Preto", "Azul", "Verde", "Mel", "Cinza"])
combo_sexo = criar_combobox(4, 1, "Sexo:", ["Masculino", "Feminino", "Outro"])

# Linha 6/7: Altura e CPF
entry_altura = criar_campo(6, 0, "Altura (m):")
entry_cpf = criar_campo(6, 1, "CPF:")


# Função para realizar cadastro
def fazer_cadastro():
    nome = entry_nome.get()
    idade = entry_idade.get()
    olhos = combo_olhos.get()
    sexo = combo_sexo.get()
    altura = entry_altura.get()
    cpf = entry_cpf.get()

    if not nome or not idade or not olhos or not sexo or not altura or not cpf:
        messagebox.showerror("Erro", "Por favor, preencha todos os campos.")
        return

    mensagem = (
        f"Nome: {nome}\n"
        f"Idade: {idade}\n"
        f"Cor dos olhos: {olhos}\n"
        f"Sexo: {sexo}\n"
        f"Altura: {altura}\n"
        f"CPF: {cpf}"
    )
    messagebox.showinfo("Cadastro realizado!", mensagem)


# Botão cadastrar
botao_cadastro = tk.Button(
    root,
    text="CADASTRAR",
    font=("Arial", 12, "bold"),
    bg="#8C05FA",
    fg="white",
    width=20,
    height=2,
    command=fazer_cadastro
)
botao_cadastro.grid(row=8, column=0, columnspan=2, pady=25)


# Texto inferior
rodape = tk.Label(
    root,
    text="Sistema de Cadastro - SENAI",
    font=("Arial", 9),
    bg="#f2f2f2",
    fg="gray"
)
rodape.grid(row=9, column=0, columnspan=2)


root.mainloop()