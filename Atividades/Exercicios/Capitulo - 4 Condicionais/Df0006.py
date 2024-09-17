Numero1 = int(input("Digite o número 1: "))
Numero2 = int(input("Digite o número 2: "))
Numero3 = int(input("Digite o número 3: "))

if Numero1 >= Numero2 and Numero1 >= Numero3:
    print(f"O numero 1: {Numero1} é o maior número!")
elif Numero2 >= Numero1 and Numero2 >= Numero3:
    print(f"O numero 2:{Numero2} é o maior número!")
else:
    print(f"O numero 3: {Numero3} é o maior número!")