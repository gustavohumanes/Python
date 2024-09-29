

Idade_Do_Jovem = int(input("Digite o valor da idade do jovem: "))

if Idade_Do_Jovem < 6:
    print("Mas já? taporra")
elif Idade_Do_Jovem < 18:
    print(f"Ainda não está na hora, espere {abs(18-Idade_Do_Jovem)} anos para isso.")
elif Idade_Do_Jovem > 18:
    print(f"Já passou a hora você está {(abs(18-Idade_Do_Jovem))} anos atrasado")
else:
    print("Está na hora de se alistar!")