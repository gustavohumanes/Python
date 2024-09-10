import random

n1 = str(input("Digite um nome: "))
n2 = str(input("Digite outro nome: "))
n3 = str(input("Mais um, bora fi: "))
n4 = str(input("Esse é o último: "))

Nomes = [n1, n2, n3, n4]

print(f" O nome escolhido foi {random.choice(Nomes)}")