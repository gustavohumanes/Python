print('\033[7;37;44mDIGITE OS VALORES ABAIXO!\033[m')

V1 = float(input("Digite o valor do lado 1: "))
V2 = float(input("Digite o valor do lado 2: "))
V3 = float(input("Digite o valor do lado 3: "))

#Verificação das somas dos lados de um triângulo!
if V1 < V2 + V3 and V1 > V2-V3:
    if V2 < V1+V3 and V2 > V1-V3:
        if V3 < V2+V1 and V3 > V2-V1:
            print("É um triângulo!")
else:
    print("Não é um triângulo")