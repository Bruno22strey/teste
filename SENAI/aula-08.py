#Laço com Índices (usando while)]
notas = [7, 8, 5, 9, 6]
x = 0
while x < 5:
    print(notas[x])
    x += 1

#Lendo Notas Dinamicamente
notas = []
x = 0
while x < 5:
    n = float(input(f"Nota {x+1}: "))
    notas.append(n)
    x += 1

soma = sum(notas)
media = soma / 5
print(f"Média: {media}")


#Cópias de Listas — Por Referência
lista = [1, 2, 3, 4, 5]
copia = lista #mesma referência!

copia[0] = 6

print(lista) # [6, 2, 3, 4, 5]
print(copia) # [6, 2, 3, 4, 5]