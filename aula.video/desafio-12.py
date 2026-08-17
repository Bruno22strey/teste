preco = float(input("Digite o preço do produto: R$ "))

desconto = preco * 0.05
novo_preco = preco - desconto

print(f"Desconto (5%): R$ {desconto:.2f}")
print(f"Novo preço: R$ {novo_preco:.2f}")