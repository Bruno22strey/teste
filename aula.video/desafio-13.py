salario = float(input("Digite o salário do funcionário: R$ "))

desconto = salario * 0.15
novo_salario = salario - desconto

print(f"Desconto (15%): R$ {desconto:.2f}")
print(f"Novo salário: R$ {novo_salario:.2f}")