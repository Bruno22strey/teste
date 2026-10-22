"""
Trabalho: Controle de Gastos Pessoais (interface tkinter)

Funcionalidades:
 1 - Adicionar Receita
 2 - Adicionar Despesa
 3 - Listar Movimentações
 4 - Consultar Saldo
 5 - Excluir Movimentação
 6 - Gerar Relatório
 0 - Sair

Os dados são salvos automaticamente em "movimentacoes.json".
"""

import json
import os
import tkinter as tk
from tkinter import ttk, messagebox

ARQUIVO = "movimentacoes.json"
FORMATO_DATA = "%d/%m/%Y %H:%M"


# ======================================================================
# LÓGICA (funções independentes da interface)
# ======================================================================

def carregar_dados():
    """Lê o JSON. Se o arquivo não existir, cria vazio. Se estiver
    vazio ou corrompido, retorna lista vazia."""
    if not os.path.exists(ARQUIVO):
        salvar_dados([])
        return []
    try:
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            dados = json.load(f)
        return dados if isinstance(dados, list) else []
    except (json.JSONDecodeError, OSError):
        return []


def salvar_dados(movimentacoes):
    """Grava a lista de movimentações no arquivo JSON."""
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(movimentacoes, f, ensure_ascii=False, indent=4)


def proximo_id(movimentacoes):
    """Gera um novo identificador numérico."""
    return max((m["id"] for m in movimentacoes), default=0) + 1


def validar_valor(texto):
    """Converte o texto em float. Retorna (valor, erro)."""
    texto = texto.strip().replace("R$", "").replace(" ", "")
    # aceita "1.234,56" e "1234.56" e "1234,56"
    if "," in texto:
        texto = texto.replace(".", "").replace(",", ".")
    try:
        valor = float(texto)
    except ValueError:
        return None, "Valor inválido! Digite apenas números."
    if valor <= 0:
        return None, "O valor deve ser maior que zero."
    return valor, None


def adicionar_movimentacao(movimentacoes, descricao, valor, tipo):
    """Cria a movimentação, adiciona na lista e salva no arquivo."""
    from datetime import datetime
    movimentacoes.append({
        "id": proximo_id(movimentacoes),
        "descricao": descricao,
        "valor": valor,
        "tipo": tipo,
        "data": datetime.now().strftime(FORMATO_DATA),
    })
    salvar_dados(movimentacoes)


def excluir_movimentacao(movimentacoes, id_mov):
    """Remove pelo id. Retorna True se encontrou."""
    for m in movimentacoes:
        if m["id"] == id_mov:
            movimentacoes.remove(m)
            salvar_dados(movimentacoes)
            return True
    return False


def total_por_tipo(movimentacoes, tipo):
    return sum(m["valor"] for m in movimentacoes if m["tipo"] == tipo)


def calcular_saldo(movimentacoes):
    """Receitas aumentam o saldo; despesas reduzem."""
    return total_por_tipo(movimentacoes, "Receita") - total_por_tipo(movimentacoes, "Despesa")


def moeda(valor):
    """Formata como R$ 2.500,00"""
    texto = f"{valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    return f"R$ {texto}"


# ======================================================================
# INTERFACE
# ======================================================================

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Controle de Gastos Pessoais")
        self.geometry("760x560")
        self.minsize(700, 520)

        self.movimentacoes = carregar_dados()

        self.var_descricao = tk.StringVar()
        self.var_valor = tk.StringVar()
        self.var_saldo = tk.StringVar()

        self.criar_widgets()
        self.atualizar_tela()
        self.protocol("WM_DELETE_WINDOW", self.sair)

    # ---------------------------------------------------------- widgets
    def criar_widgets(self):
        ttk.Label(self, text="Bem-vindo ao Controle de Gastos Pessoais!",
                  font=("Segoe UI", 15, "bold")).pack(pady=(12, 4))

        # Saldo
        self.lbl_saldo = tk.Label(self, textvariable=self.var_saldo,
                                  font=("Segoe UI", 13, "bold"))
        self.lbl_saldo.pack(pady=(0, 8))

        # Formulário
        form = ttk.LabelFrame(self, text="Nova movimentação")
        form.pack(fill="x", padx=14, pady=4)

        ttk.Label(form, text="Descrição:").grid(row=0, column=0, padx=8, pady=8, sticky="e")
        ent_desc = ttk.Entry(form, textvariable=self.var_descricao, width=32)
        ent_desc.grid(row=0, column=1, padx=4, pady=8, sticky="w")

        ttk.Label(form, text="Valor (R$):").grid(row=0, column=2, padx=8, pady=8, sticky="e")
        ttk.Entry(form, textvariable=self.var_valor, width=14).grid(
            row=0, column=3, padx=4, pady=8, sticky="w")

        ttk.Button(form, text="1 - Adicionar Receita",
                   command=lambda: self.adicionar("Receita")).grid(
            row=1, column=0, columnspan=2, padx=8, pady=(0, 8), sticky="ew")
        ttk.Button(form, text="2 - Adicionar Despesa",
                   command=lambda: self.adicionar("Despesa")).grid(
            row=1, column=2, columnspan=2, padx=8, pady=(0, 8), sticky="ew")
        form.columnconfigure(1, weight=1)

        # Lista (opção 3)
        lista = ttk.LabelFrame(self, text="3 - Movimentações")
        lista.pack(fill="both", expand=True, padx=14, pady=6)

        colunas = ("id", "data", "tipo", "valor", "descricao")
        self.tree = ttk.Treeview(lista, columns=colunas, show="headings", height=10)
        cabecalhos = {"id": ("ID", 45), "data": ("Data/Hora", 140),
                      "tipo": ("Tipo", 80), "valor": ("Valor", 110),
                      "descricao": ("Descrição", 260)}
        for col, (texto, largura) in cabecalhos.items():
            self.tree.heading(col, text=texto)
            self.tree.column(col, width=largura, anchor="w")
        self.tree.tag_configure("Receita", foreground="#1b7f3b")
        self.tree.tag_configure("Despesa", foreground="#c0392b")

        scroll = ttk.Scrollbar(lista, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scroll.set)
        self.tree.pack(side="left", fill="both", expand=True, padx=(6, 0), pady=6)
        scroll.pack(side="right", fill="y", pady=6, padx=(0, 6))

        # Botões inferiores
        barra = ttk.Frame(self)
        barra.pack(fill="x", padx=14, pady=(2, 12))
        ttk.Button(barra, text="4 - Consultar Saldo",
                   command=self.consultar_saldo).pack(side="left", padx=3)
        ttk.Button(barra, text="5 - Excluir Movimentação",
                   command=self.excluir).pack(side="left", padx=3)
        ttk.Button(barra, text="6 - Gerar Relatório",
                   command=self.gerar_relatorio).pack(side="left", padx=3)
        ttk.Button(barra, text="0 - Sair", command=self.sair).pack(side="right", padx=3)

        ent_desc.focus()

    # ------------------------------------------------------------ ações
    def atualizar_tela(self):
        """Recarrega a tabela e o saldo exibido."""
        for item in self.tree.get_children():
            self.tree.delete(item)
        for m in self.movimentacoes:
            self.tree.insert("", "end", iid=str(m["id"]), tags=(m["tipo"],),
                             values=(m["id"], m["data"], m["tipo"],
                                     moeda(m["valor"]), m["descricao"]))
        saldo = calcular_saldo(self.movimentacoes)
        self.var_saldo.set(f"Saldo atual: {moeda(saldo)}")
        self.lbl_saldo.config(fg="#1b7f3b" if saldo >= 0 else "#c0392b")

    def adicionar(self, tipo):
        descricao = self.var_descricao.get().strip()
        if not descricao:
            messagebox.showerror("Erro", "A descrição não pode ficar vazia.")
            return
        valor, erro = validar_valor(self.var_valor.get())
        if erro:
            messagebox.showerror("Erro", erro)
            return

        adicionar_movimentacao(self.movimentacoes, descricao, valor, tipo)
        self.var_descricao.set("")
        self.var_valor.set("")
        self.atualizar_tela()
        messagebox.showinfo("Sucesso", f"{tipo} cadastrada com sucesso!")

    def consultar_saldo(self):
        saldo = calcular_saldo(self.movimentacoes)
        messagebox.showinfo("Saldo", f"Saldo atual: {moeda(saldo)}")

    def excluir(self):
        selecionado = self.tree.selection()
        if not selecionado:
            messagebox.showwarning("Atenção", "Selecione uma movimentação na lista.")
            return
        id_mov = int(selecionado[0])
        if not messagebox.askyesno("Confirmar", f"Excluir a movimentação {id_mov}?"):
            return
        if excluir_movimentacao(self.movimentacoes, id_mov):
            self.atualizar_tela()
            messagebox.showinfo("Sucesso", "Movimentação excluída com sucesso!")
        else:
            messagebox.showerror("Erro", "Movimentação não encontrada.")

    def gerar_relatorio(self):
        receitas = total_por_tipo(self.movimentacoes, "Receita")
        despesas = total_por_tipo(self.movimentacoes, "Despesa")
        texto = (
            f"Total de Receitas: {moeda(receitas)}\n"
            f"Total de Despesas: {moeda(despesas)}\n"
            f"Saldo Atual: {moeda(receitas - despesas)}\n"
            f"Quantidade de Movimentações: {len(self.movimentacoes)}"
        )
        messagebox.showinfo("RELATÓRIO FINANCEIRO", texto)

    def sair(self):
        messagebox.showinfo("Até logo", "Obrigado por utilizar o Controle de Gastos Pessoais!")
        self.destroy()


if __name__ == "__main__":
    App().mainloop()