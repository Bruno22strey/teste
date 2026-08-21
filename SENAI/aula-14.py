#Operações Básicas em uma Pilha

#Toda pilha oferece quatro operações fundamentais:
#Push (Empilhar)
#Adiciona um elemento ao topo da pilha.

#Pop (Desempilhar)
#Remove e retorna o elemento do topo.

#Peek (Espiar)
#Visualiza o topo sem removê-lo.

#isEmpty
#Verifica se a pilha está vazia.


#Implementando Pilhas em Python

#A forma mais simples de criar uma pilha é usando uma lista com os métodos append() e pop():

pilha = [] # Cria pilha vazia
pilha.append(1) # Push
pilha.append(2) # Push
pilha.append(3) # Push
print(pilha) # [1, 2, 3]

topo = pilha.pop() # Pop → 3
print(topo) # 3
print(pilha) # [1, 2]

#O método pop() sem argumentos remove sempre o último elemento — comportamento LIFO nativo!



#Exemplo Prático: Inverter uma String
#Uma aplicação clássica de pilhas é inverter a ordem dos caracteres de uma string:
Texto = "PYTHON"
pilha = []
# Empilha cada caractere
for char in texto:
    pilha.append(char)
resultado = ""
# Desempilha na ordem inversa
while pilha:
    resultado += pilha.pop()
print(resultado)

Saída: "nohtyP"

#Passo 1
#Percorra a string e empilhe
#cada caractere com
#append().

#Passo 2
#Desempilhe com pop() até a
#pilha ficar vazia.

#Resultado
#A ordem natural do LIFO
#inverte a string
#automaticamente.