
while True:
    print("VERIFICADOR DE NÚMEROS PARES OU IMPARES")
    try:
        v1 = int(input("Digte o valor maior: "))
        v2 = int(input("Digite o valor menor: "))
    except ValueError:
        print("Valores incorretos, por favor digite novamente!")
        continue

    if v1 < v2:
        print("Tente novamente")
        continue
    else:
        print("Os números pares são: ")
        for c in range(v2, v1+1):
            if c % 2 == 0:
                print(f"{c} = par")
            else:
                print(f"{c} = impar")
    print("TAREFA CONCLUÍDA!")
    break