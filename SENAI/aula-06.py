#Exercício 1: De 1 a 100
x = 1
while x <= 100:
    print(x)
    x = x + 1

#Exercício 2: De 50 a 100
x = 50
while x <= 100:
    print(x)
    x = x + 1

#Exercício 3: Contagem Regressiva
x = 10
while x >= 1:
    print(x)
    x = x - 1
print('Fogo!')



#Exercício 1: Números Ímpares
x = 0
n = int(input("Digite um número: "))
while x <= n:
    if x % 2 != 0:
        print(x)
    x = x + 1

#Exercício 2: Múltiplos de 3
x = 0
while x <= 30:
    if x % 3 == 0:
        print(x)
    x = x + 1

#Contadores com Condições: Corrigindo um Teste
#pontos = 0
#questao = 1
#while questao <= 3:
    #resposta = input(f'Resposta da questão {questao} (A/B/C/D): ')
#if questao == 1 and resposta == 'b':
    #pontos = pontos + 1
#if questao == 2 and resposta == 'a':

    #pontos = pontos + 1
#if questao == 3 and resposta == 'd':
    #pontos = pontos + 1
#questao = questao+1

#print(f'O aluno fez {pontos} ponto(s)')

#Exercício: Tabuadas
t = int(input("De qual número quer a tabuada? "))
n = 1
print(f"Tabuada de {t}:")
while n <= 10:
    print(f"{t} x {n} = {t * n}")
    n += 1

#Menu Interativo com Tabuadas
def menu_tabuadas():
    while True:
        print("\n--- Menu de Tabuadas ---")
        print("1. Tabuada do 1")
        print("2. Tabuada do 2")
        print("...")
        print("10. Tabuada do 10")
        print("Sair. Sair do programa")
        escolha = input("Digite o número da tabuada que deseja (ou 'Sair'): ").lower()
        if escolha == 'sair':
            print("Saindo do menu de tabuadas.")
            break
        else:
            tipo = type(int(escolha))
            if tipo != int:
                print(" ")
                print("Entrada inválida. Por favor, digite um número ou 'Sair'.")
            else:
                numero_tabuada = int(escolha)
                if 1 <= numero_tabuada <= 10:
                    print(f"\n--- Tabuada do {numero_tabuada} ---")
                    nr = 1
                    while nr <= 10:
                        print(f"{numero_tabuada} x {nr:2} = {(numero_tabuada * nr):2}")
                        nr += 1
                else:
                    print("Número inválido. Por favor, digite um número entre 1 e 10.")


def menu_operacoes():
    while True:
        print("\n--- Gerador de Tabuadas de Operações ---")
        print("Escolha uma operação:")
        print("1. Adição")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        print("0. Sair")
        escolha_operacao = input("Digite o número da operação desejada: ").lower()
        if escolha_operacao == '0' or escolha_operacao == 'sair':
            print("Saindo do menu de operações.")
            break
        operacao = int(escolha_operacao)
        if not (0 <= operacao <= 4):
            print("Opção inválida. Por favor, escolha um número entre 0 e 4.")
            continue
        numero_base = int(input("Digite o número para o qual deseja calcular a tabuada: "))
        print(f"\n--- Tabuada para o número {numero_base} ---")
        nr = 1
        while nr <= 10:
            if operacao == 1:  # Adição
                print(f"{numero_base} + {nr:2} = {(numero_base + nr):3}")
            elif operacao == 2:  # Subtração
                print(f"{numero_base} - {nr:2} = {(numero_base - nr):3}")
            elif operacao == 3:  # Multiplicação
                print(f"{numero_base} x {nr:2} = {(numero_base * nr):3}")
            elif operacao == 4:  # Divisão
                print(f"{numero_base} / {nr:2} = {(numero_base / nr):.2f}")
            nr += 1


# --- Programa principal ---
while True:
    print("\n=== MENU PRINCIPAL ===")
    print("1. Menu de Tabuadas")
    print("2. Menu de Operações")
    print("0. Sair do programa")
    escolha_principal = input("Escolha uma opção: ").lower()

    if escolha_principal == '0' or escolha_principal == 'sair':
        print("Encerrando o programa. Até logo!")
        break
    elif escolha_principal == '1':
        menu_tabuadas()
    elif escolha_principal == '2':
        menu_operacoes()
    else:
        print("Opção inválida. Escolha 1, 2 ou 0.")