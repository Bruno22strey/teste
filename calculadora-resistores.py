import tkinter as tk
from tkinter import ttk

# Criando a janela
root = tk.Tk()
root.title("Calculadora de Resistor")
root.geometry("800x600")


# =========================
# CANVAS
# =========================

canvas = tk.Canvas(
    root,
    width=700,
    height=250,
    bg="white"
)

canvas.pack(pady=20)


# =========================
# CORES
# =========================

cores = [
    "Preto",
    "Marrom",
    "Vermelho",
    "Laranja",
    "Amarelo",
    "Verde",
    "Azul",
    "Violeta",
    "Cinza",
    "Branco"
]

cores_tolerancia = [
    "Marrom",
    "Vermelho",
    "Verde",
    "Azul",
    "Violeta",
    "Cinza",
    "Dourado",
    "Prata"
]


# =========================
# CONVERTER COR
# =========================

def converter_cor(cor):

    if cor == "Preto":
        return "black"

    elif cor == "Marrom":
        return "brown"

    elif cor == "Vermelho":
        return "red"

    elif cor == "Laranja":
        return "orange"

    elif cor == "Amarelo":
        return "yellow"

    elif cor == "Verde":
        return "green"

    elif cor == "Azul":
        return "blue"

    elif cor == "Violeta":
        return "purple"

    elif cor == "Cinza":
        return "gray"

    elif cor == "Branco":
        return "white"

    elif cor == "Dourado":
        return "gold"

    elif cor == "Prata":
        return "silver"


# =========================
# DESENHAR RESISTOR
# =========================

def desenhar_resistor():

    # Apaga o resistor anterior
    canvas.delete("all")

    # Fios
    canvas.create_line(
        50, 125,
        200, 125,
        fill="gray",
        width=5
    )

    canvas.create_line(
        500, 125,
        650, 125,
        fill="gray",
        width=5
    )

    # Corpo do resistor
    canvas.create_rectangle(
        200, 75,
        500, 175,
        fill="#F0D1B2",
        outline="black",
        width=2
    )

    # Pegando as cores escolhidas
    cor1 = converter_cor(combo1.get())
    cor2 = converter_cor(combo2.get())
    cor3 = converter_cor(combo3.get())
    cor4 = converter_cor(combo4.get())

    # Primeira faixa
    canvas.create_rectangle(
        240, 75,
        270, 175,
        fill=cor1
    )

    # Segunda faixa
    canvas.create_rectangle(
        290, 75,
        320, 175,
        fill=cor2
    )

    # Terceira faixa
    canvas.create_rectangle(
        340, 75,
        370, 175,
        fill=cor3
    )

    # Faixa de tolerância
    canvas.create_rectangle(
        450, 75,
        480, 175,
        fill=cor4
    )


# =========================
# CALCULAR RESISTOR
# =========================

def calcular():

    cor1 = combo1.get()
    cor2 = combo2.get()
    cor3 = combo3.get()
    cor4 = combo4.get()


    # =====================
    # PRIMEIRA COR
    # =====================

    if cor1 == "Preto":
        numero1 = 0

    elif cor1 == "Marrom":
        numero1 = 1

    elif cor1 == "Vermelho":
        numero1 = 2

    elif cor1 == "Laranja":
        numero1 = 3

    elif cor1 == "Amarelo":
        numero1 = 4

    elif cor1 == "Verde":
        numero1 = 5

    elif cor1 == "Azul":
        numero1 = 6

    elif cor1 == "Violeta":
        numero1 = 7

    elif cor1 == "Cinza":
        numero1 = 8

    elif cor1 == "Branco":
        numero1 = 9


    # =====================
    # SEGUNDA COR
    # =====================

    if cor2 == "Preto":
        numero2 = 0

    elif cor2 == "Marrom":
        numero2 = 1

    elif cor2 == "Vermelho":
        numero2 = 2

    elif cor2 == "Laranja":
        numero2 = 3

    elif cor2 == "Amarelo":
        numero2 = 4

    elif cor2 == "Verde":
        numero2 = 5

    elif cor2 == "Azul":
        numero2 = 6

    elif cor2 == "Violeta":
        numero2 = 7

    elif cor2 == "Cinza":
        numero2 = 8

    elif cor2 == "Branco":
        numero2 = 9


    # =====================
    # MULTIPLICADOR
    # =====================

    if cor3 == "Preto":
        multiplicador = 1

    elif cor3 == "Marrom":
        multiplicador = 10

    elif cor3 == "Vermelho":
        multiplicador = 100

    elif cor3 == "Laranja":
        multiplicador = 1000

    elif cor3 == "Amarelo":
        multiplicador = 10000

    elif cor3 == "Verde":
        multiplicador = 100000

    elif cor3 == "Azul":
        multiplicador = 1000000

    elif cor3 == "Violeta":
        multiplicador = 10000000

    elif cor3 == "Cinza":
        multiplicador = 100000000

    elif cor3 == "Branco":
        multiplicador = 1000000000


    # =====================
    # CALCULO
    # =====================

    resistencia = (numero1 * 10 + numero2) * multiplicador


    # =====================
    # TOLERÂNCIA
    # =====================

    if cor4 == "Marrom":
        tolerancia = 1

    elif cor4 == "Vermelho":
        tolerancia = 2

    elif cor4 == "Verde":
        tolerancia = 0.5

    elif cor4 == "Azul":
        tolerancia = 0.25

    elif cor4 == "Violeta":
        tolerancia = 0.1

    elif cor4 == "Cinza":
        tolerancia = 0.05

    elif cor4 == "Dourado":
        tolerancia = 5

    elif cor4 == "Prata":
        tolerancia = 10


    # =====================
    # MOSTRAR RESULTADO
    # =====================

    resultado.config(
        text="Resistência: "
        + str(resistencia)
        + " Ω ± "
        + str(tolerancia)
        + "%"
    )


    # Desenhar o resistor
    desenhar_resistor()


# =========================
# TÍTULO
# =========================

titulo = tk.Label(
    root,
    text="Calculadora de Resistor",
    font=("Arial", 20, "bold")
)

titulo.pack()


# =========================
# FRAME
# =========================

frame = tk.Frame(root)
frame.pack(pady=10)


# =========================
# PRIMEIRA FAIXA
# =========================

tk.Label(
    frame,
    text="1ª Faixa"
).grid(row=0, column=0)

combo1 = ttk.Combobox(
    frame,
    values=cores,
    state="readonly"
)

combo1.set("Marrom")

combo1.grid(
    row=1,
    column=0,
    padx=10
)


# =========================
# SEGUNDA FAIXA
# =========================

tk.Label(
    frame,
    text="2ª Faixa"
).grid(row=0, column=1)

combo2 = ttk.Combobox(
    frame,
    values=cores,
    state="readonly"
)

combo2.set("Preto")

combo2.grid(
    row=1,
    column=1,
    padx=10
)


# =========================
# TERCEIRA FAIXA
# =========================

tk.Label(
    frame,
    text="Multiplicador"
).grid(row=0, column=2)

combo3 = ttk.Combobox(
    frame,
    values=cores,
    state="readonly"
)

combo3.set("Vermelho")

combo3.grid(
    row=1,
    column=2,
    padx=10
)


# =========================
# TOLERÂNCIA
# =========================

tk.Label(
    frame,
    text="Tolerância"
).grid(row=0, column=3)

combo4 = ttk.Combobox(
    frame,
    values=cores_tolerancia,
    state="readonly"
)

combo4.set("Dourado")

combo4.grid(
    row=1,
    column=3,
    padx=10
)


# =========================
# BOTÃO
# =========================

botao = tk.Button(
    root,
    text="CALCULAR",
    command=calcular,
    font=("Arial", 12, "bold")
)

botao.pack(pady=20)


# =========================
# RESULTADO
# =========================

resultado = tk.Label(
    root,
    text="Resistência: 1000 Ω ± 5%",
    font=("Arial", 16, "bold")
)

resultado.pack()


# Desenhar o resistor inicialmente
desenhar_resistor()


# Manter a janela aberta
root.mainloop()
