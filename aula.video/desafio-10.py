reais = float(input("Digite quanto dinheiro você tem (em reais): R$ "))

cotacao_dolar = 5.08  # cotação aproximada do dólar em reais (agosto/2026)

dolares = reais / cotacao_dolar

print(f"Com R$ {reais:.2f}, você pode comprar aproximadamente US$ {dolares:.2f}")