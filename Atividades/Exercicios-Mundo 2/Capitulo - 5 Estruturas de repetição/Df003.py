# Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram de 1 até 500!
s = 0

while True:
    valor = int(input("Quantos números deseja saber a soma?"))
    for c in range(1, valor):
        if c % 2 != 0 and c % 3 == 0:
            s += c
            print(f"Impar, multiplo de 3: {c}")
        else:
            print("Impar")
    break


print(f"A soma de tudo aqui {s}")