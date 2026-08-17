import tkinter as tk
from tkinter import ttk, messagebox

# Janela principal
root = tk.Tk()
root.title("Tela de Cadastro")
root.geometry("600x350")
root.resizable(False, False)
root.configure(bg="#f2f2f2")


# Foto de perfil (esquerda, ocupando todas as linhas dos campos)
try:
    imagem = tk.PhotoImage(file="logo.png")
    imagem = imagem.subsample(2, 2)

    label_imagem = tk.Label(root, image=imagem, bg="#f2f2f2")
    label_imagem.image = imagem  # evita a imagem sumir
    label_imagem.grid(row=0, column=0, rowspan=6, padx=(20, 15), pady=10)

except Exception:
    label_imagem = tk.Label(
        root,
        text="👤\nFoto de\nperfil",
        font=("Arial", 22),
        bg="#dddddd",
        width=12,
        height=10
    )
    label_imagem.grid(row=0, column=0, rowspan=6, padx=(20, 15), pady=10)


# Função auxiliar para criar campo de texto (label à esquerda, entry à direita)
def criar_campo(linha, texto):
    label = tk.Label(root, text=texto, font=("Arial", 11), bg="#f2f2f2", width=14, anchor="w")
    label.grid(row=linha, column=1, sticky="w", padx=(5, 5), pady=10)

    entry = tk.Entry(root, font=("Arial", 11), width=22)
    entry.grid(row=linha, column=2, pady=10)
    return entry


# Função auxiliar para criar combobox (label à esquerda, combo à direita)
def criar_combobox(linha, texto, opcoes):
    label = tk.Label(root, text=texto, font=("Arial", 11), bg="#f2f2f2", width=14, anchor="w")
    label.grid(row=linha, column=1, sticky="w", padx=(5, 5), pady=10)

    combo = ttk.Combobox(root, font=("Arial", 11), width=20, values=opcoes, state="readonly")
    combo.grid(row=linha, column=2, pady=10)
    return combo


# Campos, um embaixo do outro (linhas 0 a 5), à direita da foto
entry_nome = criar_campo(0, "Nome:")
entry_idade = criar_campo(1, "Idade:")
combo_olhos = criar_combobox(2, "Cor dos olhos:", ["Castanho", "Preto", "Azul", "Verde", "Mel", "Cinza"])
combo_sexo = criar_combobox(3, "Sexo:", ["Masculino", "Feminino", "Outro"])
entry_altura = criar_campo(4, "Altura (m):")
entry_cpf = criar_campo(5, "CPF:")


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
    bg="#0509FA",
    fg="white",
    width=20,
    height=1,
    command=fazer_cadastro
)
botao_cadastro.grid(row=6, column=0, columnspan=3, pady=20)


root.mainloop()