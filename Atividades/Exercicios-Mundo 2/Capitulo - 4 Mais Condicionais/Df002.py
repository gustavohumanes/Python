print("-"*45)
print("Digite 1 para conversor em binário")
print("Digite 2 para conversor em octal")
print("Digite 3 para conversor em hexadecimal")
print("-"*45)

Conversor = int(input("Escolha o conversor que deseja: "))
#-------------------------------------------------------------------------------------
if Conversor == 1:
    Valor_Dado = int(input("Digite o número que deseja descobrir em binário: "))
    print(f"O valor em binário é: {bin(Valor_Dado)}")

elif Conversor == 2:
    Valor_Dado = int(input("Digite o número que deseja descobrir em octal: "))
    print(f"O valor em octal é: {oct(Valor_Dado)}")

elif Conversor == 3:
    Valor_Dado = int(input("Digite o número que deseja descobrir em hexadecimal: "))
    print(f"O valor em hexadecimal é: {hex(Valor_Dado)[2:].upper()}")

else:
    print("Você digitou errado ou tá fazendo gracinha, tenta novamente, OTÁRIO.")
#-------------------------------------------------------------------------------------
