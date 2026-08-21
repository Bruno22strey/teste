#fila
fila = []

fila.append("Ana")
print(fila)  # ["Ana"]

fila.append("Bruno")
print(fila)  # ["Ana", "Bruno"]

primeiro = fila.pop(0)
print(primeiro)  # "Ana"
print(fila)       # ["Bruno"]

segundo = fila.pop(0)
print(segundo)   # "Bruno"
print(fila)       # []