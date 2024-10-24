


while True:
    numero = int(input("Digite o valor do número que deseja descobrir se é ou não, primo: "))
    Primo = True

    for c in range(2, numero):
        if numero % c == 0:
            print(f"{c} testado e não é divisivel")
            Primo = False
            break
    
    if Primo:
        print("Primo")
    else:
        print("Não primo")
    continuar = input("Deseja verificar outro número? (s/n): ").lower()
    if continuar != 's':
        break