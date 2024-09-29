from random import gauss

categorias = {
    "Mirim": 0,
    "Infantil": 0,
    "Junior": 0,
    "Senior": 0,
    "Mestre": 0
}

Nadadores = []

for Player in range(10):
    Valor = abs(gauss(mu=15, sigma=15))
    Nadadores.append(Valor)

for idade in Nadadores:
    if idade < 9:
        categorias["Mirim"] += 1
    elif idade < 14:
        categorias["Infantil"] += 1
    elif idade < 20:
        categorias["Junior"] += 1
    elif idade < 21:
        categorias["Senior"] += 1
    else:
        categorias["Mestre"] += 1

print("Distribuição de nadadores por categoria:")
for categoria, quantidade in categorias.items():
    print(f"{categoria}: {quantidade} nadadores")


