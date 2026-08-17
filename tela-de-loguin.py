import tkinter as tk

root = tk.Tk()
root.title("Login")
root.resizable(False, False)

tk.Label(root, text="Faça seu login", font=("Font", 30)).pack(ipady=5, fill="x")

#subsample(5, 5) reduz a imagem para 1/5 do tamanho original (divide por 5)
image = tk.PhotoImage(file="logo.png").subsample(5, 5)
tk.Label(root, image=image, relief=tk.RAISED).pack(pady=5)

tk.Label(root, text="Usuário").pack(anchor="w", padx=30)
username_entry = tk.Entry(root)
username_entry.pack()

tk.Label(root, text="Senha").pack(anchor="w", padx=30)
password_entry = tk.Entry(root)
password_entry.pack()

tk.Button(root, text="Entrar", width=18).pack(pady=10, padx=30, fill="x")

tk.Checkbutton(root, text="Lembrar-me").pack(side="left", padx=20, pady=5)

tk.Label(root, text="Esqueceu sua senha?", fg="blue",
cursor="hand2").pack(side="right", padx=20, pady=5)


root.mainloop()
