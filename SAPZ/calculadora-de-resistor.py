# Bibliotecas usadas no programa
import tkinter as tk
from tkinter import ttk, messagebox
import math


# Cores usadas para desenhar as faixas do resistor
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


# Valor correspondente a cada cor nas duas primeiras bandas
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


# Valores usados para multiplicar a resistência
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


# Porcentagem de tolerância de cada cor
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


# Criação da janela principal
janela = tk.Tk()

janela.title("Calculadora de Resistor")
janela.geometry("650x700")
janela.resizable(False, False)
janela.configure(bg="#eef3f7")


# CONFIGURAÇÃO DOS ESTILOS

style = ttk.Style()

# Tenta usar um tema que deixa os componentes com uma aparência melhor
try:
    style.theme_use("clam")
except:
    pass


# Estilo do título
style.configure(
    "Titulo.TLabel",
    background="#eef3f7",
    foreground="#263746",
    font=("Segoe UI", 17, "bold")
)


# Estilo usado nos textos principais
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

# Frame onde ficam os campos, botões e o desenho
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


# MODO DE ENTRADA

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


# Variável que guarda o modo escolhido pelo usuário
modo = tk.StringVar(value="cores")


# Opção para informar o valor da resistência
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


# Opção para informar as cores do resistor
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


# CAMPO PARA DIGITAR O VALOR

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


# NOMES DAS BANDAS

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


# Cores que podem ser escolhidas nas duas primeiras bandas
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


# COMBOBOX DA BANDA 1

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


# COMBOBOX DA BANDA 2

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


# COMBOBOX DO MULTIPLICADOR

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


# COMBOBOX DA TOLERÂNCIA

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


# ÁREA ONDE O RESISTOR SERÁ DESENHADO

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


# FUNÇÃO PARA DESENHAR O RESISTOR

def desenhar_resistor(event=None):

    # Apaga o desenho anterior antes de fazer um novo
    canvas.delete("all")

    banda1 = combo_banda1.get()
    banda2 = combo_banda2.get()
    multiplicador = combo_multiplicador.get()
    tolerancia = combo_tolerancia.get()

    # Define algumas cores padrão caso nenhuma tenha sido selecionada
    if banda1 == "":
        banda1 = "Marrom"

    if banda2 == "":
        banda2 = "Preto"

    if multiplicador == "":
        multiplicador = "Vermelho"

    if tolerancia == "":
        tolerancia = "Dourado"


    # Desenha os fios do resistor
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


    # Desenha o corpo do resistor
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


    # Posições e cores das quatro faixas
    faixas = [
        (180, banda1),
        (220, banda2),
        (260, multiplicador),
        (360, tolerancia)
    ]


    # Desenha cada uma das faixas
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


    # Texto que aparece abaixo do resistor
    canvas.create_text(
        280,
        165,
        text="Resistor",
        fill="#555555",
        font=("Segoe UI", 10, "bold")
    )


# TRANSFORMA O VALOR DA RESISTÊNCIA EM CORES

def valor_para_cores(valor):

    # Não permite valores menores ou iguais a zero
    if valor <= 0:
        raise ValueError("O valor deve ser maior que zero.")


    # Esses valores são usados para encontrar
    # as duas primeiras casas do resistor
    multiplicador_num = 0.01
    expoente = -2


    # Aumenta o multiplicador até chegar em um número adequado
    while valor / multiplicador_num >= 100:

        multiplicador_num *= 10
        expoente += 1


    # Diminui o multiplicador se o número ainda estiver muito pequeno
    while valor / multiplicador_num < 10:

        multiplicador_num /= 10
        expoente -= 1


    numero = valor / multiplicador_num

    # Arredonda para obter dois algarismos significativos
    dois_digitos = round(numero)


    # Corrige o valor caso o arredondamento resulte em 100
    if dois_digitos >= 100:

        dois_digitos = 10
        expoente += 1


    # Separa o primeiro e o segundo algarismo
    primeiro = dois_digitos // 10
    segundo = dois_digitos % 10


    cor_banda1 = None
    cor_banda2 = None


    # Procura as cores correspondentes aos dois números
    for cor, numero_cor in VALORES.items():

        if numero_cor == primeiro:
            cor_banda1 = cor

        if numero_cor == segundo:
            cor_banda2 = cor


    # Descobre qual é a cor do multiplicador
    valor_mult = 10 ** expoente

    cor_multiplicador = None


    for cor, valor_cor in MULTIPLICADORES.items():

        # math.isclose é usado para comparar números decimais
        if math.isclose(
            valor_cor,
            valor_mult,
            rel_tol=1e-9,
            abs_tol=1e-12
        ):

            cor_multiplicador = cor
            break


    # Caso não exista uma cor para o multiplicador encontrado
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


# FORMATA O VALOR PARA FICAR MAIS FÁCIL DE LER

def formatar_resistencia(valor):

    if valor >= 1_000_000_000:

        return f"{valor / 1_000_000_000:g} GΩ"

    elif valor >= 1_000_000:

        return f"{valor / 1_000_000:g} MΩ"

    elif valor >= 1_000:

        return f"{valor / 1_000:g} kΩ"

    else:

        return f"{valor:g} Ω"


# CALCULA A RESISTÊNCIA A PARTIR DO VALOR DIGITADO

def calcular_por_valor():

    texto = entrada_valor.get().strip()


    # Verifica se o usuário deixou o campo vazio
    if texto == "":

        messagebox.showwarning(
            "Atenção",
            "Digite o valor da resistência."
        )

        return


    # Deixa tudo em letras minúsculas
    texto = texto.lower()

    # Remove algumas formas que o usuário pode usar para escrever ohm
    texto = texto.replace("Ω", "")
    texto = texto.replace("ohms", "")
    texto = texto.replace("ohm", "")
    texto = texto.strip()


    # Valor inicial do multiplicador
    multiplicador_digitado = 1


    # k representa mil
    if texto.endswith("k"):

        multiplicador_digitado = 1_000
        texto = texto[:-1]


    # m representa um milhão
    elif texto.endswith("m"):

        multiplicador_digitado = 1_000_000
        texto = texto[:-1]


    # g representa um bilhão
    elif texto.endswith("g"):

        multiplicador_digitado = 1_000_000_000
        texto = texto[:-1]


    # Tenta transformar o texto digitado em número
    try:

        valor = float(
            texto.replace(",", ".")
        )

        valor *= multiplicador_digitado


    except ValueError:

        # Mostra uma mensagem caso o valor digitado seja inválido
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


    # Verifica se o valor é válido
    if valor <= 0:

        messagebox.showerror(
            "Erro",
            "O valor deve ser maior que zero."
        )

        return


    # Tenta descobrir as cores correspondentes ao valor
    try:

        banda1, banda2, multiplicador = valor_para_cores(valor)

    except ValueError as erro:

        messagebox.showerror(
            "Erro",
            str(erro)
        )

        return


    # A tolerância padrão usada nesse modo será dourado
    tolerancia = "Dourado"


    # Atualiza as caixas de seleção
    combo_banda1.set(banda1)
    combo_banda2.set(banda2)
    combo_multiplicador.set(multiplicador)
    combo_tolerancia.set(tolerancia)


    # Atualiza o desenho
    desenhar_resistor()


    # Calcula novamente o valor representado pelas cores
    numero = (
        VALORES[banda1] * 10
        + VALORES[banda2]
    )

    resistencia_calculada = (
        numero
        * MULTIPLICADORES[multiplicador]
    )

    tolerancia_valor = TOLERANCIAS[tolerancia]


    # Mostra o resultado na tela
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


# CALCULA A RESISTÊNCIA A PARTIR DAS CORES

def calcular_por_cores():

    # Pega as cores selecionadas pelo usuário
    banda1 = combo_banda1.get()
    banda2 = combo_banda2.get()
    multiplicador = combo_multiplicador.get()
    tolerancia = combo_tolerancia.get()


    # Verifica se todas as opções foram preenchidas
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


    # Junta os valores das duas primeiras bandas
    numero = (
        VALORES[banda1] * 10
        + VALORES[banda2]
    )


    # Calcula a resistência usando o multiplicador
    resistencia = (
        numero
        * MULTIPLICADORES[multiplicador]
    )


    # Pega o valor da tolerância
    tolerancia_valor = TOLERANCIAS[tolerancia]


    # Mostra o resultado
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


    # Atualiza o desenho do resistor
    desenhar_resistor()


# FUNÇÃO PRINCIPAL DO BOTÃO

def calcular():

    # Verifica qual dos dois modos está selecionado
    if modo.get() == "valor":

        calcular_por_valor()

    else:

        calcular_por_cores()


# ALTERA O MODO DA CALCULADORA

def alterar_modo():

    # Quando o usuário escolhe informar o valor
    if modo.get() == "valor":

        # Ativa o campo de texto
        entrada_valor.config(
            state="normal"
        )


        # Desativa as opções de cores
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


    # Quando o usuário escolhe informar pelas cores
    else:

        # Desativa o campo de texto
        entrada_valor.config(
            state="disabled"
        )


        # Ativa as opções de cores
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


    # Atualiza o desenho depois de trocar o modo
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


# ÁREA DO RESULTADO

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


# BOTÃO PARA FAZER O CÁLCULO

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


# Atualiza o desenho sempre que uma cor for alterada
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


# Deixa todas as colunas com o mesmo espaço
for coluna in range(4):

    principal.grid_columnconfigure(
        coluna,
        weight=1
    )


# VALORES INICIAIS

# Define algumas cores para aparecerem quando o programa iniciar
combo_banda1.set("Marrom")
combo_banda2.set("Preto")
combo_multiplicador.set("Vermelho")
combo_tolerancia.set("Dourado")


# O programa começa no modo de escolher as cores,
# então o campo de texto começa desativado
entrada_valor.config(
    state="disabled"
)


# Desenha o resistor pela primeira vez
desenhar_resistor()


# Mantém a janela aberta
janela.mainloop()
