#Importação Completa do Módulo

#import matematica

# Acessando funções com o prefixo do módulo

#resultado = matematica.somar(5, 3)
#area = matematica.area_circulo(10)
#valor = matematica.PI

#Como funciona?

#Ao usar import matematica, você carrega todo o módulo e acessa seus membros através do prefixo matematica.

#Vantagem: evita conflitos de nomes e deixa claro de onde cada função vem.




#Importação Específica do Módulo

#Importando apenas o necessário

# matematica.py
PI = 3.14159

def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def area_circulo(raio):
    return PI * raio * raio




#Exercício 1: Módulo simples
def celsius_fahrenheit(c: float) -> float:
    """Converte temperatura em Celsius para Fahrenheit.
    Fórmula: F = C * 9/5 + 32
    """
    return c * 9 / 5 + 32


def metros_quilometros(m: float) -> float:
    """Converte distância em metros para quilômetros.
    1 km = 1000 m
    """
    return m / 1000





#Exercício 2: Pacote
import math
from typing import List, Union

Number = Union[int, float]


# ===== Aritmética =====
def soma(a: Number, b: Number) -> Number:
    return a + b


def subtrai(a: Number, b: Number) -> Number:
    return a - b


def multiplica(a: Number, b: Number) -> Number:
    return a * b


def divide(a: Number, b: Number) -> float:
    if b == 0:
        raise ValueError("Divisão por zero")
    return a / b


# ===== Geometria =====
def area_circulo(raio: Number) -> float:
    if raio < 0:
        raise ValueError("Raio não pode ser negativo")
    return math.pi * (raio ** 2)


def perimetro_circulo(raio: Number) -> float:
    if raio < 0:
        raise ValueError("Raio não pode ser negativo")
    return 2 * math.pi * raio


# ===== Estatística =====
def media(valores: List[Number]) -> float:
    if not valores:
        raise ValueError("A lista não pode ser vazia")
    return sum(valores) / len(valores)


def mediana(valores: List[Number]) -> float:
    if not valores:
        raise ValueError("A lista não pode ser vazia")
    nums = sorted(valores)
    n = len(nums)
    mid = n // 2
    if n % 2 == 1:
        return float(nums[mid])
    return (nums[mid - 1] + nums[mid]) / 2.0


# ===== Programa principal =====
def main() -> None:
    print("\nAritmética:")
    print("soma:", soma(10, 3))
    print("subtração:", subtrai(10, 3))
    print("multiplicação:", multiplica(10, 3))
    print("divisão:", divide(10, 3))

    print("\nGeometria:")
    print(f"Área do círculo (r={2.5}): {area_circulo(2.5):.4f}")
    print(f"Perímetro do círculo (r={2.5}): {perimetro_circulo(2.5):.4f}")

    valores = [1, 2, 2, 4, 5]
    print("\nEstatística:")
    print("média:", media(valores))
    print("mediana:", mediana(valores))


if __name__ == "__main__":
    main()



#==========Jogo da Velha com Matrizes============

def criar_tabuleiro():
    return [[" " for _ in range(3)] for _ in range(3)]


def exibir_tabuleiro(tabuleiro):
    print()
    for i, linha in enumerate(tabuleiro):
        print(f" {linha[0]} | {linha[1]} | {linha[2]} ")
        if i < 2:
            print("---+---+---")
    print()


def verificar_vencedor(tabuleiro, jogador):
    # Checa as 3 linhas
    for linha in tabuleiro:
        if all(celula == jogador for celula in linha):
            return True

    # Checa as 3 colunas
    for col in range(3):
        if all(tabuleiro[linha][col] == jogador for linha in range(3)):
            return True

    # Checa diagonal principal
    if all(tabuleiro[i][i] == jogador for i in range(3)):
        return True

    # Checa diagonal secundária
    if all(tabuleiro[i][2 - i] == jogador for i in range(3)):
        return True

    return False


def tabuleiro_cheio(tabuleiro):
    return all(celula != " " for linha in tabuleiro for celula in linha)


def jogar():
    tabuleiro = criar_tabuleiro()
    jogador_atual = "X"

    exibir_tabuleiro(tabuleiro)

    while True:
        print(f"Vez do jogador {jogador_atual}")

        try:
            linha = int(input("Digite a linha (0 a 2): "))
            coluna = int(input("Digite a coluna (0 a 2): "))
        except ValueError:
            print("Entrada inválida! Digite números entre 0 e 2.\n")
            continue

        if not (0 <= linha <= 2 and 0 <= coluna <= 2):
            print("Posição fora do tabuleiro! Tente novamente.\n")
            continue

        if tabuleiro[linha][coluna] != " ":
            print("Essa posição já está ocupada! Tente novamente.\n")
            continue

        tabuleiro[linha][coluna] = jogador_atual
        exibir_tabuleiro(tabuleiro)

        if verificar_vencedor(tabuleiro, jogador_atual):
            print(f"O jogador {jogador_atual} venceu!")
            break

        if tabuleiro_cheio(tabuleiro):
            print("Houve empate!")
            break

        jogador_atual = "O" if jogador_atual == "X" else "X"


if __name__ == "__main__":
    jogar()




#=========Controle de assentos no cinema=========
def criar_cinema(linhas, colunas):
    return [["L" for _ in range(colunas)] for _ in range(linhas)]


def exibir_mapa(cinema):
    print("\nMapa de assentos:")
    for linha in cinema:
        for assento in linha:
            print(assento, end=" ")
        print()


def contar_livres(cinema):
    total = 0
    for linha in cinema:
        for assento in linha:
            if assento == "L":
                total += 1
    return total


def reservar_assento(cinema, linhas, colunas):
    try:
        linha = int(input("Digite a linha (0 a 4): "))
        coluna = int(input("Digite a coluna (0 a 9): "))
    except ValueError:
        print("Entrada inválida! Digite apenas números.")
        return

    if not (0 <= linha < linhas and 0 <= coluna < colunas):
        print("Posição fora do cinema!")
        return

    if cinema[linha][coluna] == "O":
        print("Esse assento já está ocupado! Escolha outro.")
        return

    cinema[linha][coluna] = "O"
    print(f"Assento [{linha}][{coluna}] reservado com sucesso!")


def main():
    linhas = 5
    colunas = 10
    cinema = criar_cinema(linhas, colunas)

    while True:
        print("\n===== CINEMA =====")
        print("1 - Reservar assento")
        print("2 - Mostrar mapa")
        print("3 - Mostrar assentos livres")
        print("4 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            reservar_assento(cinema, linhas, colunas)
        elif opcao == "2":
            exibir_mapa(cinema)
        elif opcao == "3":
            print(f"Assentos livres: {contar_livres(cinema)}")
        elif opcao == "4":
            print("Encerrando o sistema do cinema.")
            break
        else:
            print("Opção inválida!")


if __name__ == "__main__":
    main()