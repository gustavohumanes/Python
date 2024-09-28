try:
    Valor1 = float(input("Digite um número: "))
    Valor2 = float(input("Digite outro número: "))

    if Valor1 > Valor2:
        print(f"{Valor1} é o maior")
    elif Valor2 > Valor1:
        print(f"{Valor2} é o maior")
    else:
        print(f"Os valores são iguais")
except ValueError:
    print("Comi o teu cu, é para digitar número rapa, tá maluco mo negue?")
