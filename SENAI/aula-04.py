# Exemplo 1: Verificar idade para dirigir
idade = 18
habilitacao = True

pode_dirigir = idade <= 18 and habilitacao
print(f"Pode dirigir: {pode_dirigir}")
Saída: True


#== igual

#> maior

#< menor

#>= maior ou igual

#<= menor ou igual

#!= diferente

# Exemplo 2: Sistema de login
usuario_correto = "admin"
senha_correta = "1234"
tentativa_usuario = "admin"
tentativa_senha = "5678"
acesso_permitido = (tentativa_usuario == usuario_correto) 
(tentativa_senha == senha_correta)
print(f"Acesso permitido: {acesso_permitido}")
Saída: False

# Exemplo 3: Operador OR
tem_dinheiro = False
tem_credito = True
pode_comprar = tem_dinheiro or tem_credito
print(f"Pode comprar: {pode_comprar}")
Saída: True

# Exemplo 4: Operador NOT
chuva = True

print(f"Está chovendo: {chuva}")        # Saída 1: Está chovendo: True
print(f"Não está chovendo: {not chuva}") # Saída 2: Não está chovendo: False


#Exercício 1: Variáveis Pessoais
nome = "Maria"
idade = 25
altura = 1.65

print("Nome:", nome)
print("Idade:", idade)
print("Altura:", altura)

#Se o exercício pedir para o usuário digitar os dados em vez de fixar no código:
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
altura = float(input("Digite sua altura: "))

print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"Altura: {altura}")


#Exercício 2: Operações Aritméticas
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

soma = num1 + num2
subtracao = num1 - num2
multiplicacao = num1 * num2

if num2 != 0:
    divisao = num1 / num2
    print(f"Divisão: {divisao}")
else:
    print("Divisão: impossível (divisão por zero)")

print(f"Soma: {soma}")
print(f"Subtração: {subtracao}")
print(f"Multiplicação: {multiplicacao}")



#Exercício 3: Valor Total de uma Compra
valor_unitario = float(input("Digite o valor unitário do produto: "))
quantidade = int(input("Digite a quantidade vendida: "))

valor_total = valor_unitario * quantidade

print(f"Valor total da compra: R$ {valor_total:.2f}")