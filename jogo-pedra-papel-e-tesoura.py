import tkinter as tk
import random

# Janela principal
root = tk.Tk()
root.title("Pedra, Papel ou Tesoura")
root.geometry("450x420")
root.resizable(False, False)
root.configure(bg="#f2f2f2")


opcoes = ["Pedra", "Papel", "Tesoura"]

maos = {
    "Pedra": "✊",
    "Papel": "✋",
    "Tesoura": "✌️"
}


# Título
titulo = tk.Label(
    root,
    text="Pedra, Papel ou Tesoura",
    font=("Arial", 16, "bold"),
    bg="#f2f2f2",
    fg="#1900ff"
)
titulo.pack(pady=(15, 10))


# Canvas onde o jogo acontece (fundo preto)
canvas = tk.Canvas(root, width=420, height=200, bg="black", highlightthickness=0)
canvas.pack(pady=5)

mao_jogador = canvas.create_text(110, 100, text="?", font=("Arial", 60), fill="white")
mao_computador = canvas.create_text(310, 100, text="?", font=("Arial", 60), fill="white")
x_central = canvas.create_text(210, 100, text="X", font=("Arial", 14, "bold"), fill="white")


# Label onde aparece a mensagem de quem ganhou
label_resultado = tk.Label(
    root,
    text="Escolha uma opção",
    font=("Arial", 13, "bold"),
    bg="#f2f2f2",
    fg="#333333"
)
label_resultado.pack(pady=10)


# Função que define quem venceu
def verificar_vencedor(jogador, computador):
    if jogador == computador:
        return "empate"

    vence = {
        "Pedra": "Tesoura",
        "Papel": "Pedra",
        "Tesoura": "Papel"
    }

    if vence[jogador] == computador:
        return "jogador"
    else:
        return "computador"


# Função que desenha o risco vertical do lado vencedor/perdedor
def desenhar_riscos(resultado):
    canvas.delete("risco")

    if resultado == "jogador":
        canvas.create_line(60, 20, 60, 180, fill="#00ff00", width=4, tags="risco")
        canvas.create_line(360, 20, 360, 180, fill="#ff0000", width=4, tags="risco")
    elif resultado == "computador":
        canvas.create_line(60, 20, 60, 180, fill="#ff0000", width=4, tags="risco")
        canvas.create_line(360, 20, 360, 180, fill="#00ff00", width=4, tags="risco")


# Função chamada quando o usuário clica em uma mão
def jogar(escolha_jogador):
    escolha_computador = random.choice(opcoes)
    resultado = verificar_vencedor(escolha_jogador, escolha_computador)

    canvas.itemconfig(mao_jogador, text=maos[escolha_jogador])
    canvas.itemconfig(mao_computador, text=maos[escolha_computador])

    desenhar_riscos(resultado)

    if resultado == "jogador":
        label_resultado.config(text="Você venceu!", fg="#0a8a0a")
    elif resultado == "computador":
        label_resultado.config(text="Você perdeu!", fg="#c00000")
    else:
        label_resultado.config(text="Empate!", fg="#333333")


# Frame que guarda as mãos clicáveis
frame_maos = tk.Frame(root, bg="#f2f2f2")
frame_maos.pack(pady=10)

# Cada "botão" é um Label com o emoji, sem borda e sem texto
mao_pedra = tk.Label(frame_maos, text=maos["Pedra"], font=("Arial", 40), bg="#f2f2f2", cursor="hand2")
mao_pedra.grid(row=0, column=0, padx=15)
mao_pedra.bind("<Button-1>", lambda e: jogar("Pedra"))

mao_papel = tk.Label(frame_maos, text=maos["Papel"], font=("Arial", 40), bg="#f2f2f2", cursor="hand2")
mao_papel.grid(row=0, column=1, padx=15)
mao_papel.bind("<Button-1>", lambda e: jogar("Papel"))

mao_tesoura = tk.Label(frame_maos, text=maos["Tesoura"], font=("Arial", 40), bg="#f2f2f2", cursor="hand2")
mao_tesoura.grid(row=0, column=2, padx=15)
mao_tesoura.bind("<Button-1>", lambda e: jogar("Tesoura"))


root.mainloop()