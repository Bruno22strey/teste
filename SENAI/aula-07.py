#Exercício 1 — Contando Vogais

texto = input("Digite uma frase ou palavra: ")
vogais = "aeiou"
contador = 0
texto_processado = texto.lower()
for letra in texto_processado:
    if letra in vogais:
        contador += 1
print(f"O texto digitado contém {contador} vogais.")

#Exercício 2 — Vogais e Consoantes
texto = input("Digite uma frase ou palavra: ")
vogais_ref = "aeiou"
consoantes_ref = "bcdfghjklmnpqrstvwxyz"
total_vogais = 0
total_consoantes = 0
texto_minusculo = texto.lower()
for letra in texto_minusculo:
    if letra in vogais_ref:
        total_vogais += 1
    elif letra in consoantes_ref:
        total_consoantes += 1

print("\n--- Resultado da Contagem ---")
print(f"Vogais encontradas: {total_vogais}")
print(f"Consoantes encontradas: {total_consoantes}")

#Exercício 3 — Maior número

maior = None

for i in range(5):
    num = int(input("Digite um número: "))
if maior is None or num > maior:
    maior = num
print("Maior número:", maior)

#Exercício 4 — Par ou impar

pares = 0
impares = 0
for i in range(10):
    num = int(input("Digite um número: "))
if num % 2 == 0:
    pares += 1
else:
    impares += 1
print("Pares:", pares)
print("Ímpares:", impares)