largura = float(input("Digite a largura da parede (em metros): "))
altura = float(input("Digite a altura da parede (em metros): "))

area = largura * altura
tinta_necessaria = area / 2

print(f"Área da parede: {area:.2f} m²")
print(f"Tinta necessária: {tinta_necessaria:.2f} litros")