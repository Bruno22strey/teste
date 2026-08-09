import tkinter as tk
from tkinter import messagebox

# Janela principal
root = tk.Tk()
root.title("Tela de Login")
root.geometry("400x500")
root.resizable(False, False)
root.configure(bg="#f2f2f2")


# Título
titulo = tk.Label(
    root,
    text="SENAI - Sistemas",
    font=("Arial", 20, "bold"),
    bg="#f2f2f2",
    fg="#1a1a1a"
)
titulo.pack(pady=(20, 10))


# Foto / Logo
try:
    imagem = tk.PhotoImage(file="logo.png")
    imagem = imagem.subsample(3, 3)

    label_imagem = tk.Label(
        root,
        image=imagem,
        bg="#f2f2f2"
    )
    label_imagem.pack(pady=10)

except:
    label_imagem = tk.Label(
        root,
        text="📷\nFoto",
        font=("Arial", 30),
        bg="#dddddd",
        width=10,
        height=4
    )
    label_imagem.pack(pady=10)


# Campo usuário
label_usuario = tk.Label(
    root,
    text="Usuário:",
    font=("Arial", 12),
    bg="#f2f2f2"
)
label_usuario.pack(pady=(10, 5))

entry_usuario = tk.Entry(
    root,
    font=("Arial", 12),
    width=30
)
entry_usuario.pack()


# Campo senha
label_senha = tk.Label(
    root,
    text="Senha:",
    font=("Arial", 12),
    bg="#f2f2f2"
)
label_senha.pack(pady=(15, 5))

entry_senha = tk.Entry(
    root,
    font=("Arial", 12),
    width=30,
    show="*"
)
entry_senha.pack()


# Função para realizar login
def fazer_login():
    usuario = entry_usuario.get()
    senha = entry_senha.get()

    if usuario == "admin" and senha == "1234":
        messagebox.showinfo(
            "Login",
            "Login realizado com sucesso!"
        )
    else:
        messagebox.showerror(
            "Erro",
            "Usuário ou senha incorretos."
        )


# Botão entrar
botao_login = tk.Button(
    root,
    text="ENTRAR",
    font=("Arial", 12, "bold"),
    bg="#0066cc",
    fg="white",
    width=20,
    height=2,
    command=fazer_login
)
botao_login.pack(pady=25)


# Texto inferior
rodape = tk.Label(
    root,
    text="Sistema de Login - SENAI",
    font=("Arial", 9),
    bg="#f2f2f2",
    fg="gray"
)
rodape.pack()


root.mainloop()