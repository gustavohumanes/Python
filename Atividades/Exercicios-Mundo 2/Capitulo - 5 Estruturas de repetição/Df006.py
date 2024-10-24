Termo_Incial = int(input("Digite o termo inicial da P.A: "))
Razao = int(input("Digite a razao da P.A: "))
Lista_Valores_PA = []
s = 0

for c in range(0, 10):
    s = c*Razao
    Lista_Valores_PA.append(Termo_Incial+s)


print(f"Valo de cada um: {Lista_Valores_PA}")
