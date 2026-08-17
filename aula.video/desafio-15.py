dias = int(input("Digite a quantidade de dias alugados: "))
km = float(input("Digite a quantidade de km percorridos: "))

preco_dias = dias * 60
preco_km = km * 0.15

total = preco_dias + preco_km

print(f"Valor por dias: R$ {preco_dias:.2f}")
print(f"Valor por km rodado: R$ {preco_km:.2f}")
print(f"Total a pagar: R$ {total:.2f}")