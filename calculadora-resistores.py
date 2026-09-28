import tkinter as tk
from tkinter import ttk

# ------------------------------------------------------------
# DADOS (tabelas de cores)
# ------------------------------------------------------------

# Cor -> número (usado nas 2 primeiras faixas e no multiplicador)
digitos = {
    "preto": 0, "marrom": 1, "vermelho": 2, "laranja": 3, "amarelo": 4,
    "verde": 5, "azul": 6, "violeta": 7, "cinza": 8, "branco": 9
}

# Multiplicadores especiais
mult_especial = {"dourado": 0.1, "prateado": 0.01}

# Cor -> tolerância em %
tolerancias = {
    "marrom": 1, "vermelho": 2, "verde": 0.5, "azul": 0.25,
    "violeta": 0.1, "cinza": 0.05, "dourado": 5, "prateado": 10
}

# Cor -> código de cor usado para pintar na tela
cores_hex = {
    "preto": "#111111", "marrom": "#8B4513", "vermelho": "#e53935",
    "laranja": "#fb8c00", "amarelo": "#fdd835", "verde": "#43a047",
    "azul": "#1e88e5", "violeta": "#8e24aa", "cinza": "#9e9e9e",
    "branco": "#ffffff", "dourado": "#d4af37", "prateado": "#c0c0c0"
}

# Listas que vão aparecer nas caixas de seleção
lista_digitos = list(digitos.keys())
lista_mult = list(digitos.keys()) + ["dourado", "prateado"]
lista_tol = list(tolerancias.keys())

# Cores da interface (fica fácil mudar o tema aqui)
COR_FUNDO = "#eef2f7"
COR_CABECALHO = "#1f2a44"
COR_DESTAQUE = "#26a69a"
COR_INATIVO = "#cfd8dc"


# ------------------------------------------------------------
# FUNÇÕES
# ------------------------------------------------------------

def formatar(ohms):
    """Transforma o valor em texto com Ω, kΩ ou MΩ."""
    if ohms >= 1000000:
        return f"{ohms / 1000000:.2f} MΩ"
    elif ohms >= 1000:
        return f"{ohms / 1000:.2f} kΩ"
    else:
        return f"{ohms:.2f} Ω"


def desenhar(lista_cores):
    """Desenha o resistor. Recebe uma lista com 4 cores (ou None para vazio)."""
    canvas.delete("all")  # apaga o desenho anterior

    # fio do resistor
    canvas.create_line(15, 100, 365, 100, width=6, fill="#90a4ae")

    # corpo do resistor (2 bolinhas nas pontas + retângulo no meio)
    canvas.create_oval(60, 55, 120, 145, fill="#f5deb3", outline="#8d6e63", width=2)
    canvas.create_oval(260, 55, 320, 145, fill="#f5deb3", outline="#8d6e63", width=2)
    canvas.create_rectangle(90, 55, 290, 145, fill="#f5deb3", outline="")
    canvas.create_line(90, 55, 290, 55, fill="#8d6e63", width=2)
    canvas.create_line(90, 145, 290, 145, fill="#8d6e63", width=2)

    # posição (x) de cada faixa
    posicoes = [115, 155, 195, 250]

    for i in range(4):
        if lista_cores is None:
            cor_faixa = "#dddddd"  # faixa vazia
        else:
            cor_faixa = cores_hex[lista_cores[i]]
            # nome da cor embaixo da faixa
            canvas.create_text(posicoes[i] + 9, 165, text=lista_cores[i],
                               font=("Arial", 8), fill="#455a64")
        canvas.create_rectangle(posicoes[i], 55, posicoes[i] + 18, 145,
                                fill=cor_faixa, outline="#333333")


def atualizar_previa(evento, combo, quadrado):
    """Pinta o quadradinho ao lado da caixa com a cor escolhida."""
    cor = combo.get()
    quadrado.config(bg=cores_hex[cor])


def mostrar_modo(modo):
    """Troca entre os dois modos (cores -> valor / valor -> cores)."""
    # limpa os textos e o desenho
    texto_resultado.config(text="—", fg="#90a4ae")
    texto_detalhe.config(text="Preencha os dados e clique no botão.", fg="#607d8b")
    desenhar(None)

    if modo == "cores":
        frame_valor.pack_forget()
        frame_cores.pack(fill="x")
        botao_modo1.config(bg=COR_DESTAQUE, fg="white")
        botao_modo2.config(bg=COR_INATIVO, fg="#37474f")
    else:
        frame_cores.pack_forget()
        frame_valor.pack(fill="x")
        botao_modo2.config(bg=COR_DESTAQUE, fg="white")
        botao_modo1.config(bg=COR_INATIVO, fg="#37474f")


def calcular_valor():
    """MODO 1: pega as cores escolhidas e calcula a resistência."""
    cor1 = combo_b1.get()
    cor2 = combo_b2.get()
    cor_mult = combo_mult.get()
    cor_tol = combo_tol1.get()

    # verifica se falta alguma cor
    if cor1 == "" or cor2 == "" or cor_mult == "" or cor_tol == "":
        texto_resultado.config(text="Ops!", fg="#e53935")
        texto_detalhe.config(text="Escolha todas as cores.", fg="#e53935")
        return

    # junta os dois primeiros dígitos (ex: 2 e 2 -> 22)
    numero = digitos[cor1] * 10 + digitos[cor2]

    # pega o multiplicador
    if cor_mult in mult_especial:
        multiplicador = mult_especial[cor_mult]
    else:
        multiplicador = 10 ** digitos[cor_mult]

    valor = numero * multiplicador

    texto_resultado.config(text=formatar(valor), fg="#1f2a44")
    texto_detalhe.config(text=f"Tolerância de ±{tolerancias[cor_tol]}%", fg="#607d8b")
    desenhar([cor1, cor2, cor_mult, cor_tol])


def calcular_cores():
    """MODO 2: pega o valor digitado e descobre as cores."""
    texto = entrada_valor.get().replace(",", ".")  # aceita vírgula

    # tenta converter o texto em número
    try:
        valor = float(texto)
    except ValueError:
        texto_resultado.config(text="Ops!", fg="#e53935")
        texto_detalhe.config(text="Digite um número válido.", fg="#e53935")
        return

    if valor <= 0:
        texto_resultado.config(text="Ops!", fg="#e53935")
        texto_detalhe.config(text="O valor deve ser maior que zero.", fg="#e53935")
        return

    cor_tol = combo_tol2.get()
    if cor_tol == "":
        texto_resultado.config(text="Ops!", fg="#e53935")
        texto_detalhe.config(text="Escolha a tolerância.", fg="#e53935")
        return

    # ajusta o valor para ficar entre 10 e 99 (dois dígitos)
    expoente = 0
    while valor >= 100:
        valor = valor / 10
        expoente = expoente + 1
    while valor < 10:
        valor = valor * 10
        expoente = expoente - 1

    numero = round(valor)
    if numero == 100:  # caso o arredondamento passe de 99
        numero = 10
        expoente = expoente + 1

    # separa os dígitos (ex: 47 -> 4 e 7)
    d1 = numero // 10
    d2 = numero % 10

    # descobre o nome das cores
    cor1 = lista_digitos[d1]
    cor2 = lista_digitos[d2]

    if expoente == -1:
        cor_mult = "dourado"
    elif expoente == -2:
        cor_mult = "prateado"
    elif 0 <= expoente <= 9:
        cor_mult = lista_digitos[expoente]
    else:
        texto_resultado.config(text="Ops!", fg="#e53935")
        texto_detalhe.config(text="Valor fora do limite do resistor.", fg="#e53935")
        return

    texto_resultado.config(text=f"{cor1} • {cor2} • {cor_mult}", fg="#1f2a44")
    texto_detalhe.config(text=f"Tolerância: {cor_tol} (±{tolerancias[cor_tol]}%)", fg="#607d8b")
    desenhar([cor1, cor2, cor_mult, cor_tol])


# ------------------------------------------------------------
# JANELA PRINCIPAL
# ------------------------------------------------------------
janela = tk.Tk()
janela.title("Calculadora de Resistor")
janela.geometry("800x470")
janela.config(bg=COR_FUNDO)
janela.resizable(False, False)

# ------------------------------------------------------------
# CABEÇALHO (faixa escura no topo)
# ------------------------------------------------------------
cabecalho = tk.Frame(janela, bg=COR_CABECALHO, height=70)
cabecalho.pack(fill="x")

tk.Label(cabecalho, text="⚡ Calculadora de Resistor", bg=COR_CABECALHO,
         fg="white", font=("Segoe UI", 18, "bold")).pack(side="left", padx=20, pady=15)
tk.Label(cabecalho, text="Resistores de 4 faixas", bg=COR_CABECALHO,
         fg="#90a4ae", font=("Segoe UI", 10)).pack(side="right", padx=20)

# ------------------------------------------------------------
# ÁREA PRINCIPAL (2 cards lado a lado)
# ------------------------------------------------------------
corpo = tk.Frame(janela, bg=COR_FUNDO)
corpo.pack(fill="both", expand=True, padx=20, pady=20)

# ---------- CARD DA ESQUERDA (entrada de dados) ----------
card_esq = tk.Frame(corpo, bg="white", padx=20, pady=15)
card_esq.pack(side="left", fill="y")

tk.Label(card_esq, text="Como deseja informar?", bg="white",
         font=("Segoe UI", 11, "bold"), fg="#37474f").pack(anchor="w", pady=(0, 8))

# botões que trocam o modo
frame_modos = tk.Frame(card_esq, bg="white")
frame_modos.pack(fill="x", pady=(0, 15))

botao_modo1 = tk.Button(frame_modos, text="Cores → Valor", font=("Segoe UI", 10, "bold"),
                        relief="flat", width=14, cursor="hand2",
                        command=lambda: mostrar_modo("cores"))
botao_modo1.pack(side="left", padx=(0, 5))

botao_modo2 = tk.Button(frame_modos, text="Valor → Cores", font=("Segoe UI", 10, "bold"),
                        relief="flat", width=14, cursor="hand2",
                        command=lambda: mostrar_modo("valor"))
botao_modo2.pack(side="left")

# ---------- FRAME DO MODO 1: cores -> valor ----------
frame_cores = tk.Frame(card_esq, bg="white")

# cada linha: texto + caixa de seleção + quadradinho de prévia da cor
tk.Label(frame_cores, text="Faixa 1", bg="white", font=("Segoe UI", 10)).grid(row=0, column=0, sticky="w", pady=6)
combo_b1 = ttk.Combobox(frame_cores, values=lista_digitos, state="readonly", width=12)
combo_b1.grid(row=0, column=1, padx=8)
previa1 = tk.Label(frame_cores, bg="#eeeeee", width=3, relief="solid", bd=1)
previa1.grid(row=0, column=2)

tk.Label(frame_cores, text="Faixa 2", bg="white", font=("Segoe UI", 10)).grid(row=1, column=0, sticky="w", pady=6)
combo_b2 = ttk.Combobox(frame_cores, values=lista_digitos, state="readonly", width=12)
combo_b2.grid(row=1, column=1, padx=8)
previa2 = tk.Label(frame_cores, bg="#eeeeee", width=3, relief="solid", bd=1)
previa2.grid(row=1, column=2)

tk.Label(frame_cores, text="Multiplicador", bg="white", font=("Segoe UI", 10)).grid(row=2, column=0, sticky="w", pady=6)
combo_mult = ttk.Combobox(frame_cores, values=lista_mult, state="readonly", width=12)
combo_mult.grid(row=2, column=1, padx=8)
previa3 = tk.Label(frame_cores, bg="#eeeeee", width=3, relief="solid", bd=1)
previa3.grid(row=2, column=2)

tk.Label(frame_cores, text="Tolerância", bg="white", font=("Segoe UI", 10)).grid(row=3, column=0, sticky="w", pady=6)
combo_tol1 = ttk.Combobox(frame_cores, values=lista_tol, state="readonly", width=12)
combo_tol1.grid(row=3, column=1, padx=8)
previa4 = tk.Label(frame_cores, bg="#eeeeee", width=3, relief="solid", bd=1)
previa4.grid(row=3, column=2)

# quando escolher uma cor, pinta o quadradinho
combo_b1.bind("<<ComboboxSelected>>", lambda e: atualizar_previa(e, combo_b1, previa1))
combo_b2.bind("<<ComboboxSelected>>", lambda e: atualizar_previa(e, combo_b2, previa2))
combo_mult.bind("<<ComboboxSelected>>", lambda e: atualizar_previa(e, combo_mult, previa3))
combo_tol1.bind("<<ComboboxSelected>>", lambda e: atualizar_previa(e, combo_tol1, previa4))

botao_calc1 = tk.Button(frame_cores, text="Calcular resistência", command=calcular_valor,
                        bg=COR_DESTAQUE, fg="white", font=("Segoe UI", 11, "bold"),
                        relief="flat", cursor="hand2", pady=6)
botao_calc1.grid(row=4, column=0, columnspan=3, sticky="ew", pady=(15, 0))

# ---------- FRAME DO MODO 2: valor -> cores ----------
frame_valor = tk.Frame(card_esq, bg="white")

tk.Label(frame_valor, text="Valor (Ω)", bg="white", font=("Segoe UI", 10)).grid(row=0, column=0, sticky="w", pady=6)
entrada_valor = tk.Entry(frame_valor, width=15, font=("Segoe UI", 11), relief="solid", bd=1)
entrada_valor.grid(row=0, column=1, padx=8)

tk.Label(frame_valor, text="Tolerância", bg="white", font=("Segoe UI", 10)).grid(row=1, column=0, sticky="w", pady=6)
combo_tol2 = ttk.Combobox(frame_valor, values=lista_tol, state="readonly", width=12)
combo_tol2.grid(row=1, column=1, padx=8)

botao_calc2 = tk.Button(frame_valor, text="Calcular cores", command=calcular_cores,
                        bg=COR_DESTAQUE, fg="white", font=("Segoe UI", 11, "bold"),
                        relief="flat", cursor="hand2", pady=6)
botao_calc2.grid(row=2, column=0, columnspan=2, sticky="ew", pady=(15, 0))

# ---------- CARD DA DIREITA (resultado + desenho) ----------
card_dir = tk.Frame(corpo, bg="white", padx=20, pady=15)
card_dir.pack(side="left", fill="both", expand=True, padx=(20, 0))

tk.Label(card_dir, text="RESULTADO", bg="white", fg="#90a4ae",
         font=("Segoe UI", 9, "bold")).pack(anchor="w")

texto_resultado = tk.Label(card_dir, text="—", bg="white", fg="#90a4ae",
                           font=("Segoe UI", 22, "bold"))
texto_resultado.pack(anchor="w")

texto_detalhe = tk.Label(card_dir, text="", bg="white", font=("Segoe UI", 10))
texto_detalhe.pack(anchor="w", pady=(0, 10))

canvas = tk.Canvas(card_dir, width=380, height=190, bg="#f7f9fb", highlightthickness=0)
canvas.pack()

# ------------------------------------------------------------
# INÍCIO DO PROGRAMA
# ------------------------------------------------------------
mostrar_modo("cores")  # começa no modo 1
janela.mainloop()      # mantém a janela aberta