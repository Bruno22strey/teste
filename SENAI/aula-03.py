#=========python básico=========

# Solicita três notas ao usuário
nota1 = float(input("Informe a primeira nota: "))
nota2 = float(input("Informe a segunda nota: "))
nota3 = float(input("Informe a terceira nota: "))
# Calcula a média
media = (nota1 + nota2 + nota3) / 3
# Exibe o resultado
print(f"A média é: {media:.2f}")


#=========python avançado=========

# Criando uma lista de notas usando compreensão de lista
notas = [float(input(f"Digite a nota {i+1}: ")) for i in range(3)]
# Calcula a média das notas em uma linha
media = sum(notas) / len(notas)
# Exibe o resultado formatado
print(f"A média das notas é: {media:.2f}")



#Exercício 1: Dobro de um Número
numero = float(input("Digite um número: "))
dobro = numero * 2
print(f"O dobro de {numero} é {dobro}")



#Exercício 2: Celsius para Fahrenheit
celsius = float(input("Digite a temperatura em Celsius: "))
fahrenheit = celsius * 9/5 + 32
print(f"{celsius}°C equivalem a {fahrenheit}°F")



#Exercício 3: Área de um Retângulo
base = float(input("Digite a base: "))
altura = float(input("Digite a altura: "))
area = base * altura
print(f"A área do retângulo é {area}")



#Exercício 4: Calcular Troco
total = float(input("Digite o valor total da compra: "))
pago = float(input("Digite o valor pago: "))

if pago >= total:
    troco = pago - total
    print(f"Troco a devolver: R$ {troco:.2f}")
else:
    print("Valor pago insuficiente!")



    #Exercício 5: Média Ponderada
    nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

peso1, peso2, peso3 = 2, 3, 5

media = (nota1 * peso1 + nota2 * peso2 + nota3 * peso3) / (peso1 + peso2 + peso3)
print(f"A média ponderada é {media:.2f}")



#Exercício 6: Calcular IMC
peso = float(input("Digite seu peso (kg): "))
altura = float(input("Digite sua altura (m): "))

imc = peso / (altura * altura)

if imc < 25:
    classificacao = "peso normal"
else:
    classificacao = "sobrepeso"

print(f"Seu IMC é {imc:.2f} — classificação: {classificacao}")