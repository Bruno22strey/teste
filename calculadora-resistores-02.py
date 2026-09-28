import tkinter as tk
from tkinter import ttk, messagebox
import math


# CORES

CORES = {
    "Preto": "#000000",
    "Marrom": "#8B4513",
    "Vermelho": "#E53935",
    "Laranja": "#F57C00",
    "Amarelo": "#FBC02D",
    "Verde": "#43A047",
    "Azul": "#1E88E5",
    "Violeta": "#8E44AD",
    "Cinza": "#808080",
    "Branco": "#FFFFFF",
    "Dourado": "#D4AF37",
    "Prata": "#C0C0C0"
}


# VALORES DAS CORES

VALORES = {
    "Preto": 0,
    "Marrom": 1,
    "Vermelho": 2,
    "Laranja": 3,
    "Amarelo": 4,
    "Verde": 5,
    "Azul": 6,
    "Violeta": 7,
    "Cinza": 8,
    "Branco": 9
}


# MULTIPLICADORES

MULTIPLICADORES = {
    "Prata": 0.01,
    "Dourado": 0.1,
    "Preto": 1,
    "Marrom": 10,
    "Vermelho": 100,
    "Laranja": 1000,
    "Amarelo": 10000,
    "Verde": 100000,
    "Azul": 1000000,
    "Violeta": 10000000,
    "Cinza": 100000000,
    "Branco": 1000000000
}


# TOLERÂNCIAS


TOLERANCIAS = {
    "Marrom": 1,
    "Vermelho": 2,
    "Verde": 0.5,
    "Azul": 0.25,
    "Violeta": 0.1,
    "Cinza": 0.05,
    "Dourado": 5,
    "Prata": 10
}


# JANELA

janela = tk.Tk()

janela.title("Calculadora de Resistor")

janela.geometry("650x700")

janela.resizable(False, False)

janela.configure(bg="#eef3f7")


# ESTILOS


style = ttk.Style()

try:
    style.theme_use("clam")
except:
    pass


style.configure(
    "Titulo.TLabel",
    background="#eef3f7",
    foreground="#263746",
    font=("Segoe UI", 17, "bold")
)

style.configure(
    "Pergunta.TLabel",
    background="white",
    foreground="#263746",
    font=("Segoe UI", 10, "bold")
)

style.configure(
    "TLabel",
    background="white",
    foreground="#263746",
    font=("Segoe UI", 10)
)


# TÍTULO


ttk.Label(
    janela,
    text="Calculadora de Resistor",
    style="Titulo.TLabel"
).pack(
    anchor="w",
    padx=28,
    pady=(20, 12)
)


# PAINEL PRINCIPAL


principal = tk.Frame(
    janela,
    bg="white",
    highlightbackground="#d5dde5",
    highlightthickness=1
)

principal.pack(
    fill="both",
    expand=True,
    padx=22,
    pady=(0, 22)
)



# PERGUNTA

ttk.Label(
    principal,
    text="Como deseja informar o resistor?",
    style="Pergunta.TLabel"
).grid(
    row=0,
    column=0,
    columnspan=4,
    sticky="w",
    padx=15,
    pady=(15, 5)
)


# MODO


modo = tk.StringVar(value="cores")


# RADIO - VALOR


ttk.Radiobutton(
    principal,
    text="Valor da resistência",
    variable=modo,
    value="valor",
    command=lambda: alterar_modo()
).grid(
    row=1,
    column=0,
    sticky="w",
    padx=15
)


# RADIO - CORES

ttk.Radiobutton(
    principal,
    text="Cores do resistor",
    variable=modo,
    value="cores",
    command=lambda: alterar_modo()
).grid(
    row=1,
    column=1,
    sticky="w"
)


# CAMPO DE VALOR


entrada_valor = ttk.Entry(
    principal,
    width=25
)

entrada_valor.grid(
    row=2,
    column=0,
    columnspan=2,
    sticky="w",
    padx=15,
    pady=10
)


# LABELS

ttk.Label(
    principal,
    text="Banda 1:"
).grid(
    row=3,
    column=0,
    sticky="w",
    padx=15
)

ttk.Label(
    principal,
    text="Banda 2:"
).grid(
    row=3,
    column=1,
    sticky="w"
)

ttk.Label(
    principal,
    text="Multiplicador:"
).grid(
    row=3,
    column=2,
    sticky="w"
)

ttk.Label(
    principal,
    text="Tolerância:"
).grid(
    row=3,
    column=3,
    sticky="w"
)



# LISTA DE CORES DAS BANDAS


lista_cores = [
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



# COMBO BANDA 1


combo_banda1 = ttk.Combobox(
    principal,
    values=lista_cores,
    state="readonly",
    width=12
)

combo_banda1.grid(
    row=4,
    column=0,
    padx=15,
    pady=5
)



# COMBO BANDA 2


combo_banda2 = ttk.Combobox(
    principal,
    values=lista_cores,
    state="readonly",
    width=12
)

combo_banda2.grid(
    row=4,
    column=1,
    pady=5
)



# COMBO MULTIPLICADOR

combo_multiplicador = ttk.Combobox(
    principal,
    values=list(MULTIPLICADORES.keys()),
    state="readonly",
    width=12
)

combo_multiplicador.grid(
    row=4,
    column=2,
    pady=5
)



# COMBO TOLERÂNCIA


combo_tolerancia = ttk.Combobox(
    principal,
    values=list(TOLERANCIAS.keys()),
    state="readonly",
    width=12
)

combo_tolerancia.grid(
    row=4,
    column=3,
    pady=5
)



# CANVAS

canvas = tk.Canvas(
    principal,
    width=560,
    height=190,
    bg="#f8fafc",
    highlightbackground="#d8e0e7",
    highlightthickness=1
)

canvas.grid(
    row=5,
    column=0,
    columnspan=4,
    padx=15,
    pady=(20, 10)
)



# DESENHAR RESISTOR

def desenhar_resistor(event=None):

    canvas.delete("all")

    banda1 = combo_banda1.get()
    banda2 = combo_banda2.get()
    multiplicador = combo_multiplicador.get()
    tolerancia = combo_tolerancia.get()

    # Valores padrão
    if banda1 == "":
        banda1 = "Marrom"

    if banda2 == "":
        banda2 = "Preto"

    if multiplicador == "":
        multiplicador = "Vermelho"

    if tolerancia == "":
        tolerancia = "Dourado"

    
    # FIOS
    
    canvas.create_line(
        30, 95,
        145, 95,
        fill="#777777",
        width=5
    )

    canvas.create_line(
        415, 95,
        530, 95,
        fill="#777777",
        width=5
    )

   
    # CORPO DO RESISTOR
    
    canvas.create_polygon(
        145, 65,
        160, 52,
        400, 52,
        415, 65,
        415, 125,
        400, 138,
        160, 138,
        145, 125,
        fill="#D6AE78",
        outline="#85633F",
        width=2
    )

   
    # FAIXAS
    
    faixas = [
        (180, banda1),
        (220, banda2),
        (260, multiplicador),
        (360, tolerancia)
    ]

    for x, cor in faixas:

        canvas.create_rectangle(
            x,
            52,
            x + 18,
            138,
            fill=CORES.get(cor, "#000000"),
            outline="#555555",
            width=1
        )

    
    # NOME
    

    canvas.create_text(
        280,
        165,
        text="Resistor",
        fill="#555555",
        font=("Segoe UI", 10, "bold")
    )



# CONVERTER VALOR PARA RESISTOR DE 4 BANDAS

def valor_para_cores(valor):

    if valor <= 0:
        raise ValueError("O valor deve ser maior que zero.")

    
    # Encontra um multiplicador que deixe os dois primeiros dígitos entre 10 e 99.
    

    multiplicador_num = 0.01
    expoente = -2

    while valor / multiplicador_num >= 100:
        multiplicador_num *= 10
        expoente += 1

    while valor / multiplicador_num < 10:
        multiplicador_num /= 10
        expoente -= 1

    numero = valor / multiplicador_num

    
    # Arredonda para dois algarismos significativos
    

    dois_digitos = round(numero)

    # Caso o arredondamento vire 100
    if dois_digitos >= 100:
        dois_digitos = 10
        expoente += 1

    primeiro = dois_digitos // 10
    segundo = dois_digitos % 10

    
    # Descobre a cor das duas primeiras bandas
    

    cor_banda1 = None
    cor_banda2 = None

    for cor, numero_cor in VALORES.items():

        if numero_cor == primeiro:
            cor_banda1 = cor

        if numero_cor == segundo:
            cor_banda2 = cor

    
    # Descobre a cor do multiplicador
    

    valor_mult = 10 ** expoente

    cor_multiplicador = None

    for cor, valor_cor in MULTIPLICADORES.items():

        if math.isclose(
            valor_cor,
            valor_mult,
            rel_tol=1e-9,
            abs_tol=1e-12
        ):
            cor_multiplicador = cor
            break

    if cor_multiplicador is None:
        raise ValueError(
            "Esse valor não pode ser representado "
            "com um resistor de 4 bandas."
        )

    return (
        cor_banda1,
        cor_banda2,
        cor_multiplicador
    )



# FORMATAR RESISTÊNCIA

def formatar_resistencia(valor):

    if valor >= 1_000_000_000:

        return f"{valor / 1_000_000_000:g} GΩ"

    elif valor >= 1_000_000:

        return f"{valor / 1_000_000:g} MΩ"

    elif valor >= 1_000:

        return f"{valor / 1_000:g} kΩ"

    else:

        return f"{valor:g} Ω"



# CALCULAR PELO VALOR DIGITADO

def calcular_por_valor():

    texto = entrada_valor.get().strip()

    if texto == "":
        messagebox.showwarning(
            "Atenção",
            "Digite o valor da resistência."
        )
        return

    
    # Aceita:
    #
    # 470
    # 470 ohm
    # 4.7k
    # 4.7 k
    # 1M
    # 2.2M
   
    texto = texto.lower()

    texto = texto.replace("Ω", "")
    texto = texto.replace("ohms", "")
    texto = texto.replace("ohm", "")
    texto = texto.strip()

    multiplicador_digitado = 1

    if texto.endswith("k"):

        multiplicador_digitado = 1_000
        texto = texto[:-1]

    elif texto.endswith("m"):

        multiplicador_digitado = 1_000_000
        texto = texto[:-1]

    elif texto.endswith("g"):

        multiplicador_digitado = 1_000_000_000
        texto = texto[:-1]

    try:

        valor = float(
            texto.replace(",", ".")
        )

        valor *= multiplicador_digitado

    except ValueError:

        messagebox.showerror(
            "Erro",
            "Digite um valor válido.\n\n"
            "Exemplos:\n"
            "470\n"
            "1k\n"
            "4.7k\n"
            "10k\n"
            "1M"
        )

        return

    if valor <= 0:

        messagebox.showerror(
            "Erro",
            "O valor deve ser maior que zero."
        )

        return

    try:

        banda1, banda2, multiplicador = valor_para_cores(valor)

    except ValueError as erro:

        messagebox.showerror(
            "Erro",
            str(erro)
        )

        return

    
    # Define a tolerância padrão como Dourado
    
    tolerancia = "Dourado"

    
    # Atualiza as caixas
   
    combo_banda2.set(banda2)
    combo_multiplicador.set(multiplicador)
    combo_tolerancia.set(tolerancia)

    # --------------------------------------------------------
    # Desenha o resistor
    # --------------------------------------------------------

    desenhar_resistor()

    
    # Calcula o valor efetivamente representado
    
    numero = (
        VALORES[banda1] * 10
        + VALORES[banda2]
    )

    resistencia_calculada = (
        numero
        * MULTIPLICADORES[multiplicador]
    )

    tolerancia_valor = TOLERANCIAS[tolerancia]

    
    # Mostra resultado
    
    resultado.config(
        text=(
            f"Resistência: "
            f"{formatar_resistencia(resistencia_calculada)}\n"
            f"Tolerância: ±{tolerancia_valor:g}%\n\n"
            f"Bandas: {banda1} | {banda2} | "
            f"{multiplicador} | {tolerancia}"
        ),
        fg="#263746"
    )



# CALCULAR PELO CÓDIGO DE CORES

def calcular_por_cores():

    banda1 = combo_banda1.get()
    banda2 = combo_banda2.get()
    multiplicador = combo_multiplicador.get()
    tolerancia = combo_tolerancia.get()

    if (
        banda1 == ""
        or banda2 == ""
        or multiplicador == ""
        or tolerancia == ""
    ):

        messagebox.showwarning(
            "Atenção",
            "Selecione todas as cores do resistor."
        )

        return

    
    # Primeiros dois dígitos
    

    numero = (
        VALORES[banda1] * 10
        + VALORES[banda2]
    )

    
    # Multiplicador
    
    resistencia = (
        numero
        * MULTIPLICADORES[multiplicador]
    )

    
    # Tolerância
    

    tolerancia_valor = TOLERANCIAS[tolerancia]

   
    # Resultado
   
    resultado.config(
        text=(
            f"Resistência: "
            f"{formatar_resistencia(resistencia)}\n"
            f"Tolerância: ±{tolerancia_valor:g}%\n\n"
            f"Bandas: {banda1} | {banda2} | "
            f"{multiplicador} | {tolerancia}"
        ),
        fg="#263746"
    )

    
    # Desenha resistor
   

    desenhar_resistor()



# BOTÃO CALCULAR


def calcular():

    if modo.get() == "valor":

        calcular_por_valor()

    else:

        calcular_por_cores()



# ALTERAR MODO


def alterar_modo():

    if modo.get() == "valor":

        entrada_valor.config(
            state="normal"
        )

        combo_banda1.config(
            state="disabled"
        )

        combo_banda2.config(
            state="disabled"
        )

        combo_multiplicador.config(
            state="disabled"
        )

        combo_tolerancia.config(
            state="disabled"
        )

        texto_instrucao.config(
            text="Digite o valor da resistência."
        )

        resultado.config(
            text="Digite um valor e clique em "
                 "'Calcular resistência'."
        )

    else:

        entrada_valor.config(
            state="disabled"
        )

        combo_banda1.config(
            state="readonly"
        )

        combo_banda2.config(
            state="readonly"
        )

        combo_multiplicador.config(
            state="readonly"
        )

        combo_tolerancia.config(
            state="readonly"
        )

        texto_instrucao.config(
            text="Selecione as cores do resistor."
        )

        resultado.config(
            text="Aguarde o cálculo da resistência."
        )

    desenhar_resistor()



# TEXTO DE INSTRUÇÃO

texto_instrucao = ttk.Label(
    principal,
    text="Selecione as cores do resistor.",
    style="Pergunta.TLabel"
)

texto_instrucao.grid(
    row=6,
    column=0,
    columnspan=4,
    sticky="w",
    padx=15,
    pady=(5, 8)
)



# RESULTADO

resultado = tk.Label(
    principal,
    text="Aguarde o cálculo da resistência.",
    bg="#f8fafc",
    fg="#858b91",
    font=("Segoe UI", 11),
    justify="center",
    pady=15
)

resultado.grid(
    row=7,
    column=0,
    columnspan=4,
    sticky="ew",
    padx=15,
    pady=(0, 10)
)



# BOTÃO

botao = tk.Button(
    principal,
    text="Calcular resistência",
    command=calcular,
    bg="#35B6A4",
    fg="white",
    activebackground="#299C8D",
    activeforeground="white",
    font=("Segoe UI", 10, "bold"),
    relief="flat",
    cursor="hand2",
    padx=12,
    pady=7
)

botao.grid(
    row=8,
    column=0,
    sticky="w",
    padx=15,
    pady=(5, 15)
)



# ATUALIZAR DESENHO QUANDO ALTERAR COR 

combo_banda1.bind(
    "<<ComboboxSelected>>",
    desenhar_resistor
)

combo_banda2.bind(
    "<<ComboboxSelected>>",
    desenhar_resistor
)

combo_multiplicador.bind(
    "<<ComboboxSelected>>",
    desenhar_resistor
)

combo_tolerancia.bind(
    "<<ComboboxSelected>>",
    desenhar_resistor
)


# CONFIGURAÇÃO DAS COLUNAS

for coluna in range(4):

    principal.grid_columnconfigure(
        coluna,
        weight=1
    )


# VALORES INICIAIS

combo_banda1.set("Marrom")
combo_banda2.set("Preto")
combo_multiplicador.set("Vermelho")
combo_tolerancia.set("Dourado")


# CAMPO DESABILITADO INICIALMENTE
entrada_valor.config(
    state="disabled"
)


# DESENHA RESISTOR INICIAL

desenhar_resistor()


# INICIAR

janela.mainloop()