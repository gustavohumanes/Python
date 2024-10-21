from random import choice

print("--------------------------JOKENPO-----------------------------")

while True:
    Escolha_Jogador = str(input("Digite aqui: ")).upper()
    Escolha_Maquina = choice(["PEDRA", "PAPEL", "TESOURA"])

    if Escolha_Jogador in ["PEDRA", "PAPEL", "TESOURA"]:
        if Escolha_Jogador == Escolha_Maquina:
            print("Empate")
        elif Escolha_Jogador == "PEDRA" and Escolha_Maquina == "PAPEL":
            print("Máquina venceu")
        elif Escolha_Jogador == "TESOURA" and Escolha_Maquina == "PEDRA":
            print("Máquina venceu")
        elif Escolha_Jogador == "PAPEL" and Escolha_Maquina == "TESOURA":
            print("Máquina venceu")
        else:
            print("Jogador venceu")
    else:
        print("Digite novamente porfavor!")
        continue
    print(f"Máquina escolheu {Escolha_Maquina}")
    break

print("--------------------------------------------------------------")