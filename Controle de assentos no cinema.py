linhas = 5
colunas = 10

# Criação do mapa de assentos
cinema = []

for i in range(linhas):
    linha = []

    for j in range(colunas):
        linha.append("L")  # L = Livre

    cinema.append(linha)


# Função para exibir o mapa e contar assentos livres
def exibir_mapa_e_livres(cinema_mapa):
    print("\nMapa de assentos:")

    assentos_livres = 0

    for linha_mapa in cinema_mapa:
        for assento_mapa in linha_mapa:
            print(assento_mapa, end=" ")

            if assento_mapa == "L":
                assentos_livres += 1

        print()

    print(f"\nTotal de assentos livres: {assentos_livres}")


# Início do sistema
print("Bem-vindo ao sistema de reserva de assentos do cinema!")

exibir_mapa_e_livres(cinema)


# Sistema de reservas
while True:
    try:
        linha_escolhida = int(
            input(
                f"\nDigite a linha (0 a {linhas - 1}) "
                "para reservar (-1 para sair): "
            )
        )

        if linha_escolhida == -1:
            break

        coluna_escolhida = int(
            input(
                f"Digite a coluna (0 a {colunas - 1}) "
                "para reservar: "
            )
        )

        # Verifica se linha e coluna estão dentro dos limites
        if not (
            0 <= linha_escolhida < linhas
            and 0 <= coluna_escolhida < colunas
        ):
            print(
                "Entrada inválida. Linha ou coluna fora dos limites. "
                "Tente novamente."
            )
            continue

        # Verifica se o assento está livre
        if cinema[linha_escolhida][coluna_escolhida] == "L":
            cinema[linha_escolhida][coluna_escolhida] = "O"

            print(
                f"Assento na linha {linha_escolhida}, "
                f"coluna {coluna_escolhida} reservado com sucesso!"
            )

        else:
            print(
                f"O assento na linha {linha_escolhida}, "
                f"coluna {coluna_escolhida} já está ocupado."
            )

        # Mostra o mapa atualizado
        exibir_mapa_e_livres(cinema)

    except ValueError:
        print(
            "Entrada inválida. Por favor, digite um número inteiro."
        )

    except Exception as e:
        print(f"Ocorreu um erro: {e}")


print("\nObrigado por usar o sistema de reserva de assentos.")