import tkinter as tk
from tkinter import messagebox
from tkinter import ttk


def salvar_cadastro():
    # Coleta os dados de cada componente da tela
    nome = entry_nome.get()
    genero = combo_genero.get()
    aceitou_termos = var_termos.get()
    nivel_prioridade = round(scale_prioridade.get())

    # Validação simples para garantir que o nome não está vazio
    if not nome.strip():
        messagebox.showwarning("Aviso", "Por favor, digite o seu nome!")
        return

    # Validação para garantir que aceitou os termos
    if not aceitou_termos:
        messagebox.showerror(
            "Erro", "Você precisa aceitar os termos para continuar."
        )
        return

    # Mensagem de sucesso mostrando todos os dados coletados
    resumo = (
        f"Nome: {nome}\n"
        f"Gênero: {genero}\n"
        f"Nível de Prioridade: {nivel_prioridade}\n"
        f"Termos Aceitos: Sim"
    )
    messagebox.showinfo("Cadastro Realizado", resumo)


# 1. Configuração da Janela Principal
janela = tk.Tk()
janela.title("Sistema de Cadastro Moderno")
janela.geometry("450x500")

# Define um espaçamento interno global para a janela
janela.config(padx=20, pady=20)

# Usando um estilo para deixar o visual mais limpo
estilo = ttk.Style()
estilo.theme_use("clam")

# --- TÍTULO PRINCIPAL ---
label_titulo = ttk.Label(
    janela, text="Formulário de Registro", font=("Arial", 16, "bold")
)
label_titulo.pack(pady=(0, 20))

# --- CAMPO 1: CAIXA DE TEXTO (Entry) ---
label_nome = ttk.Label(janela, text="Nome Completo:", font=("Arial", 10))
label_nome.pack(anchor="w", pady=(5, 2))

entry_nome = ttk.Entry(janela, width=40)
entry_nome.pack(fill="x", pady=(0, 15))

# --- CAMPO 2: CAIXA DE SELEÇÃO SUSPENSA (Combobox) ---
label_genero = ttk.Label(janela, text="Gênero:", font=("Arial", 10))
label_genero.pack(anchor="w", pady=(5, 2))

opcoes_genero = ["Masculino", "Feminino", "Não Informar", "Outro"]
combo_genero = ttk.Combobox(janela, values=opcoes_genero, state="readonly")
combo_genero.current(0)  # Define "Masculino" como padrão inicial
combo_genero.pack(fill="x", pady=(0, 15))

# --- CAMPO 3: BARRA DE ARRASTAR VALORES (Scale) ---
label_prioridade = ttk.Label(
    janela, text="Nível de Prioridade do Chamado (0 a 10):", font=("Arial", 10)
)
label_prioridade.pack(anchor="w", pady=(5, 2))

scale_prioridade = ttk.Scale(janela, from_=0, to=10, orient="horizontal")
scale_prioridade.set(5)  # Inicia no meio da barra (5)
scale_prioridade.pack(fill="x", pady=(0, 20))

# --- CAMPO 4: CAIXA DE MARCAR (Checkbutton) ---
var_termos = tk.BooleanVar()  # Variável especial para guardar True ou False
check_termos = ttk.Checkbutton(
    janela, text="Aceito os termos e condições de uso.", variable=var_termos
)
check_termos.pack(anchor="w", pady=(0, 25))

# --- BOTÃO DE AÇÃO ---
# Criando um botão estilizado para salvar os dados
botao_salvar = ttk.Button(
    janela, text="Salvar Cadastro", command=salvar_cadastro
)
botao_salvar.pack(fill="x", ipady=5)

# Executa e mantém a tela aberta
janela.mainloop()
