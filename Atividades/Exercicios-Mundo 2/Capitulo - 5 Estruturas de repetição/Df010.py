Lista = []

for c in range(1, 5+1):
    Peso_Da_Pessoa = int(input(f"Digite o peso da pessoa {c}: "))
    Lista.append(Peso_Da_Pessoa)

print(f"A ordem será de peso será: {sorted(Lista)}, sendo {sorted(Lista)[0]} a mais leve, e {sorted(Lista)[-1]} a mais pesada.")