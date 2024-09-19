Velocidade_Do_Carro = float(input("Digite o valor da velocidade do carro em 'Km/h' "))
Diferença_de_Velocidade = Velocidade_Do_Carro - 80

if Velocidade_Do_Carro > 80:
    print(f"Você foi multado, e terá que pagar {float(Diferença_de_Velocidade*7)}")
else:
    print("Pode seguir em frente!")
