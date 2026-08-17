import tkinter as tk

# Janela principal
root = tk.Tk()
root.title("Calculadora")
root.geometry("320x480")
root.resizable(False, False)
root.configure(bg="black")


# Variável que guarda a expressão digitada
expressao = ""


# Visor
visor = tk.Entry(
    root,
    font=("Arial", 32),
    borderwidth=0,
    bg="black",
    fg="white",
    justify="right",
    insertbackground="white"
)
visor.pack(fill="both", ipady=30, padx=10, pady=(20, 10))


# Funções dos botões
def clicar(valor):
    global expressao
    expressao += str(valor)
    visor.delete(0, tk.END)
    visor.insert(tk.END, expressao)


def limpar():
    global expressao
    expressao = ""
    visor.delete(0, tk.END)


def apagar():
    global expressao
    expressao = expressao[:-1]
    visor.delete(0, tk.END)
    visor.insert(tk.END, expressao)


def porcentagem():
    global expressao
    try:
        resultado = str(eval(expressao) / 100)
        expressao = resultado
        visor.delete(0, tk.END)
        visor.insert(tk.END, expressao)
    except Exception:
        visor.delete(0, tk.END)
        visor.insert(tk.END, "Erro")
        expressao = ""


def inverter_sinal():
    global expressao
    try:
        resultado = str(eval(expressao) * -1)
        expressao = resultado
        visor.delete(0, tk.END)
        visor.insert(tk.END, expressao)
    except Exception:
        pass


def calcular():
    global expressao
    try:
        resultado = str(eval(expressao))
        visor.delete(0, tk.END)
        visor.insert(tk.END, resultado)
        expressao = resultado
    except Exception:
        visor.delete(0, tk.END)
        visor.insert(tk.END, "Erro")
        expressao = ""


# Frame que guarda os botões
frame_botoes = tk.Frame(root, bg="black")
frame_botoes.pack(expand=True, fill="both")


# Cores no estilo iPhone
COR_FUNCAO = "#a5a5a5"       # AC, +/-, %
COR_FUNCAO_TEXTO = "black"
COR_NUMERO = "#333333"       # 0-9
COR_NUMERO_TEXTO = "white"
COR_OPERADOR = "#ff9500"     # + - x ÷ =
COR_OPERADOR_TEXTO = "white"


# Função para criar um botão padronizado
def criar_botao(texto, linha, coluna, cor_fundo, cor_texto, comando, colspan=1):
    botao = tk.Button(
        frame_botoes,
        text=texto,
        font=("Arial", 20),
        bg=cor_fundo,
        fg=cor_texto,
        borderwidth=0,
        activebackground=cor_fundo,
        activeforeground=cor_texto,
        command=comando
    )
    botao.grid(
        row=linha, column=coluna, columnspan=colspan,
        sticky="nsew", padx=3, pady=3
    )


# Configura o grid para os botões crescerem igualmente
for i in range(5):
    frame_botoes.rowconfigure(i, weight=1)
for i in range(4):
    frame_botoes.columnconfigure(i, weight=1)


# Linha 0: AC, +/-, %, ÷
criar_botao("AC", 0, 0, COR_FUNCAO, COR_FUNCAO_TEXTO, limpar)
criar_botao("+/-", 0, 1, COR_FUNCAO, COR_FUNCAO_TEXTO, inverter_sinal)
criar_botao("%", 0, 2, COR_FUNCAO, COR_FUNCAO_TEXTO, porcentagem)
criar_botao("÷", 0, 3, COR_OPERADOR, COR_OPERADOR_TEXTO, lambda: clicar("/"))

# Linha 1: 7, 8, 9, x
criar_botao("7", 1, 0, COR_NUMERO, COR_NUMERO_TEXTO, lambda: clicar(7))
criar_botao("8", 1, 1, COR_NUMERO, COR_NUMERO_TEXTO, lambda: clicar(8))
criar_botao("9", 1, 2, COR_NUMERO, COR_NUMERO_TEXTO, lambda: clicar(9))
criar_botao("×", 1, 3, COR_OPERADOR, COR_OPERADOR_TEXTO, lambda: clicar("*"))

# Linha 2: 4, 5, 6, -
criar_botao("4", 2, 0, COR_NUMERO, COR_NUMERO_TEXTO, lambda: clicar(4))
criar_botao("5", 2, 1, COR_NUMERO, COR_NUMERO_TEXTO, lambda: clicar(5))
criar_botao("6", 2, 2, COR_NUMERO, COR_NUMERO_TEXTO, lambda: clicar(6))
criar_botao("-", 2, 3, COR_OPERADOR, COR_OPERADOR_TEXTO, lambda: clicar("-"))

# Linha 3: 1, 2, 3, +
criar_botao("1", 3, 0, COR_NUMERO, COR_NUMERO_TEXTO, lambda: clicar(1))
criar_botao("2", 3, 1, COR_NUMERO, COR_NUMERO_TEXTO, lambda: clicar(2))
criar_botao("3", 3, 2, COR_NUMERO, COR_NUMERO_TEXTO, lambda: clicar(3))
criar_botao("+", 3, 3, COR_OPERADOR, COR_OPERADOR_TEXTO, lambda: clicar("+"))

# Linha 4: 0 (ocupa 2 colunas), ., =
criar_botao("0", 4, 0, COR_NUMERO, COR_NUMERO_TEXTO, lambda: clicar(0), colspan=2)
criar_botao(".", 4, 2, COR_NUMERO, COR_NUMERO_TEXTO, lambda: clicar("."))
criar_botao("=", 4, 3, COR_OPERADOR, COR_OPERADOR_TEXTO, calcular)


root.mainloop()