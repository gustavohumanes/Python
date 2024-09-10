Numero = str(input("Digite um número de 0 a 9999: "))
Numeros = [Numero[0], Numero[1], Numero[2], Numero[3]]

if(len(Numero) >= 5):
    print("Isso tem mais de 5 digitos")
else:
    print(Numeros)
    print(Numero[0])
    print(Numero[1])
    print(Numero[2])
    print(Numero[3])