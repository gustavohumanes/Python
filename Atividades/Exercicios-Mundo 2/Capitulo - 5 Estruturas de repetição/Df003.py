# Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram de 1 até 500!
s = 0
b = 0
for c in range(1, 500+1):
    b += c
    if c % 3 == 0 and c % 2 != 0:
        print(f"múltiplo de 3 e impar: {c} esse número é monstro!")
        s += c
    else:
        print(f"Sai daqui Número: {c}")

print(f"a soma dessa porra toda é {s}, a média disso tudo é {b//2}")