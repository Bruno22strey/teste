#Exercício 1: Matriz 3×3 Formatada
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Matriz 3x3:\n")
for linha in matriz:
    for elemento in linha:
        print(f"[{elemento}]\t", end="")
    print()

#Exercício 2: Somando os Elementos
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

soma = 0
print("Matriz 3x3:\n")
for linha in matriz:
    for elemento in linha:
        print(f"{elemento}\t", end="")
        soma += elemento
    print()

print("\nSoma de todos os elementos:", soma)

#Exercício 3: Buscando um Número
matriz = [
    [10, 2, 30, 4, 5],
    [6, 17, 8, 9, 10],
    [11, 12, 23, 14, 15],
    [16, 27, 18, 19, 20],
    [21, 22, 33, 24, 25]
]

numero = int(input("Digite um número inteiro: "))
encontrado = False

for i in range(5):  # linhas
    for j in range(5):  # colunas
        if matriz[i][j] == numero:
            print(f"O número {numero} existe na posição [{i}, {j}]")
            encontrado = True

if not encontrado:
    print(f"O número {numero} não existe na matriz.")


#Exercício 4: Controle de Assentos do Cinema

# Criar a matriz 5x10 preenchida com "L"
linhas = 5
colunas = 10
cinema = []
for i in range(linhas):
    linha = []
    for j in range(colunas):
        linha.append("L")
    cinema.append(linha)

# Pedir ao usuário a linha e a coluna
linha_escolhida = int(input("Digite a linha (0 a 4): "))
coluna_escolhida = int(input("Digite a coluna (0 a 9): "))

# Marcar o assento como ocupado
cinema[linha_escolhida][coluna_escolhida] = "O"

# Exibir o mapa de assentos
print("\nMapa de assentos:")
for linha in cinema:
    for assento in linha:
        print(assento, end=" ")
    print()