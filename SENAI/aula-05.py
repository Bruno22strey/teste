#Exercício 1: Positivo ou Negativo
numero = float(input("Digite um número: "))

if numero > 0:
    print("O número é positivo")
elif numero < 0:
    print("O número é negativo")
else:
    print("O número é zero")

#Exercício 2: Situação do Aluno
nota = float(input("Digite a nota do aluno: "))

if nota >= 7:
    print("Aprovado")
elif nota >= 5:
    print("Recuperação")
else:
    print("Reprovado")

#Exercício 3: Faixa Etária
idade = int(input("Digite a idade: "))

if idade <= 12:
    print("Criança")
elif idade <= 17:
    print("Adolescente")
else:
    print("Adulto")