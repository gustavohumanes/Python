#Solulção minha!
from time import sleep
from random import randint

Valor_Dado = int(input("Qual número a máquina pensou? "))
NumeroRandom = randint(0, 5) # Seleciona um número aleatório entre dois números dados

print("PROCESSANDO...")

sleep(3)
if Valor_Dado == NumeroRandom:
    print("Você acertou!")
else:
    print(f"Você errou, eu pensei no {NumeroRandom} e não no {Valor_Dado}!")