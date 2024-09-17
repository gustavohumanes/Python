#Solulção minha!

import random

Valor_Dado = int(input("Qual número a máquina pensou? "))
NumeroRandom = random.randint(0, 5)

if Valor_Dado == NumeroRandom:
    print("Você acertou!")
else:
    print("Você errou!")