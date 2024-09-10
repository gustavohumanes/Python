Numero = int(input("Digite um número de 0 a 9999: "))

print(f"Unidade: { Numero // 1 % 10}")
print(f"Dezena: { Numero // 10 % 10}")
print(f"Centena: { Numero // 100 % 10}")
print(f"Milhar: { Numero // 1000 % 10}")