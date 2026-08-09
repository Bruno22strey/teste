def desenha_linha(limite, preenchimento, largura):
    print(limite + (preenchimento * (largura - 2)) + limite)


colunas = 20
linhas = 3

desenha_linha("+", "-", colunas)

for l in range(linhas):
    desenha_linha("|", " ", colunas)

desenha_linha("+", "-", colunas)