
v1 = float(input("Digite o valor do lado 1: "))
v2 = float(input("Digite o valor do lado 2: "))
v3 = float(input("Digite o valor do lado 3: "))

if v1 + v2 > v3 and v2 + v3 > v1 and v1 + v3 > v2:
    print("Preenche os requerimentos para se formar um triângulo.")
    if v1 == v2 == v3:
        print("Triângulo equilatero!")
    elif v3 != v2 != v1:
        print("Triângulo Escaleno!")
    else:
        print("Triângulo Isosceles!")
else:
    print("Não pode ser triângulo.")
