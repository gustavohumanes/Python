Valor = 0
Valores_Somados = []

for c in range(1, 6+1):
    s = int(input(f"Digite um valor {c}: "))
    if s % 2 == 0:
        Valor += s
        Valores_Somados.append(s)

print(f"Valor é {Valor}, os valores somados foram {Valores_Somados}")

