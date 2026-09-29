# -*- coding: utf-8 -*-
"""
Trabalho Prático: Simulador de Caixa Eletrônico
Usa: variáveis, if/elif/else, laços while e persistência de dados em arquivo.
"""

ARQUIVO_SALDOS = "saldos.txt"   # arquivo onde os saldos ficam salvos (conta;saldo)
SALDO_INICIAL = 1000            # saldo fictício para contas ainda não utilizadas
CEDULAS = [100, 50, 20, 10, 5, 2]  # cédulas disponíveis no caixa


# ---------------------------------------------------------------
# Funções de arquivo
# ---------------------------------------------------------------
def carregar_saldo(conta):
    """Busca o saldo da conta no arquivo. Se não existir, retorna o saldo fictício."""
    try:
        with open(ARQUIVO_SALDOS, "r", encoding="utf-8") as arq:
            for linha in arq:
                partes = linha.strip().split(";")
                if len(partes) == 2 and partes[0] == conta:
                    return int(partes[1])
    except FileNotFoundError:
        pass  # arquivo ainda não existe: ninguém usou o caixa antes
    return SALDO_INICIAL


def salvar_saldo(conta, saldo):
    """Grava o novo saldo da conta, mantendo as demais contas do arquivo."""
    contas = {}
    try:
        with open(ARQUIVO_SALDOS, "r", encoding="utf-8") as arq:
            for linha in arq:
                partes = linha.strip().split(";")
                if len(partes) == 2:
                    contas[partes[0]] = partes[1]
    except FileNotFoundError:
        pass

    contas[conta] = str(saldo)

    with open(ARQUIVO_SALDOS, "w", encoding="utf-8") as arq:
        for c, s in contas.items():
            arq.write(c + ";" + s + "\n")


# ---------------------------------------------------------------
# Funções auxiliares
# ---------------------------------------------------------------
def formatar(valor):
    """Formata o valor como R$ 1250,00."""
    return "R$ " + str(valor) + ",00"


def ler_valor(mensagem):
    """
    Lê um valor inteiro positivo.
    Retorna o número, ou None se for inválido (já exibe a mensagem de erro).
    """
    texto = input(mensagem).strip()

    try:
        valor = int(texto)
    except ValueError:
        # Não é inteiro: pode ser fracionário (250.75) ou texto qualquer
        try:
            float(texto.replace(",", "."))
            print("Erro: Valores fracionários não são aceitos. Digite um valor inteiro.")
        except ValueError:
            print("Erro: Valor inválido. Digite apenas números inteiros.")
        return None

    if valor <= 0:
        print("Erro: Valores negativos ou zero não são aceitos.")
        return None

    return valor


def calcular_cedulas(valor):
    """
    Calcula quantas cédulas de cada tipo são necessárias (método guloso).
    Retorna uma lista de (cédula, quantidade), ou None se não for possível
    pagar o valor exato com as cédulas disponíveis (ex.: R$ 1, R$ 11).
    """
    resultado = []
    restante = valor
    i = 0
    while i < len(CEDULAS):
        qtd = restante // CEDULAS[i]
        if qtd > 0:
            resultado.append((CEDULAS[i], qtd))
            restante = restante % CEDULAS[i]
        i += 1

    if restante != 0:
        return None
    return resultado


def mostrar_menu():
    print("\nMENU")
    print("1 - Consultar saldo")
    print("2 - Sacar")
    print("3 - Depositar")
    print("4 - Sair")


# ---------------------------------------------------------------
# Programa principal
# ---------------------------------------------------------------
def main():
    # Laço externo: volta para a tela de conta e senha após "Sair"
    while True:
        print("\nBem-vindo ao Caixa Eletrônico!")
        conta = input("Digite sua conta: ").strip()
        senha = input("Digite sua senha: ")  # não é validada (conforme enunciado)

        saldo = carregar_saldo(conta)
        sair = False

        # Laço do menu: repete até o usuário escolher "Sair"
        while not sair:
            mostrar_menu()
            opcao = input("\nEscolha uma opção: ").strip()

            if opcao == "1":
                # ----- Consultar saldo -----
                print("\nSeu saldo atual é: " + formatar(saldo))

            elif opcao == "2":
                # ----- Sacar -----
                valor = ler_valor("\nDigite o valor para saque: ")
                if valor is not None:
                    if valor > saldo:
                        print("Erro: Saldo insuficiente para este saque.")
                    else:
                        cedulas = calcular_cedulas(valor)
                        if cedulas is None:
                            print("Erro: O caixa não trabalha com este valor. "
                                  "Use cédulas de R$100, R$50, R$20, R$10, R$5 e R$2.")
                        else:
                            saldo = saldo - valor
                            print("Saque realizado com sucesso.")
                            print("Entregar:")
                            for nota, qtd in cedulas:
                                if qtd == 1:
                                    print("1 cédula de R$" + str(nota))
                                else:
                                    print(str(qtd) + " cédulas de R$" + str(nota))
                            print("Saldo atual: " + formatar(saldo))

            elif opcao == "3":
                # ----- Depositar -----
                valor = ler_valor("\nDigite o valor para depósito: ")
                if valor is not None:
                    saldo = saldo + valor
                    print("Depósito realizado com sucesso!")
                    print("Saldo atual: " + formatar(saldo))

            elif opcao == "4":
                # ----- Sair: salva o saldo no arquivo -----
                salvar_saldo(conta, saldo)
                print("\nObrigado por usar nosso sistema!")
                print("Retornando para tela de conta e senha...")
                sair = True
                continue

            else:
                print("Opção inválida! Por favor, escolha uma opção de 1 a 4.")
                continue

            input("\nPressione ENTER para retornar")


main()