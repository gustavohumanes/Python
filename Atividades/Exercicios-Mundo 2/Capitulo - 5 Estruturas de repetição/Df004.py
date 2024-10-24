v1 = int(input("Digite um valor que deseja saber a tabudada: "))
Limite = int(input(f"Até quanto você deseja a tabuada de {v1}? "))

for c in range(1, Limite+1):
    print(f"{v1}x{c} = {v1*c}")