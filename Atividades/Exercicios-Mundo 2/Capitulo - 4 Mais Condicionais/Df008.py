Massa = float(input("Por favor informe sua massa corporea?(Kg) "))
Altura = float(input("Por favor informe usa altura em metros: "))

if Altura == 0 or Massa == 0:
    print("Os dados de altura ou peso estão invalidos!")
else:
    IMC = (Massa)/(Altura)**2
    if IMC < 18.5:
        print("Abaixo do peso!")
    elif IMC < 25:
        print("Peso ideal!")
    elif IMC < 30:
        print("Excesso de peso!")
    elif IMC > 35:
        print("Obesidade mórbida!")
    elif IMC >= 30:
        print("Sobre-peso!")
    print(f"Seu IMC é {IMC}")
