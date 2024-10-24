
quantidade = int(input("Quantidades de pesssoas que tem: "))

while True:
    for c in range(0, quantidade):
        while True:
            Nome = str(input("Digite o seu nome aqui! >"))
            if Nome.isalpha():
                break
            else:
                print("Valor invalido, tente novamente!")
                continue

        try:
            while True:
                Idade = int(input("Digite a sua idadeaqui! >"))
                if Idade > 125:
                    print("Valor incorreto")
                    continue
                break
        except ValueError:
            print("O valor de idade passado está incorreto")

            while True:
                Escolha = str(input("Digite M para Masculino, F para Femino >"))
                if Escolha not in ["F", "M"]:
                    print("Valo incorreto")
                    continue
                break
    break

Pessoa = {
    "Nome": Nome,
    "Idade": 0,
    "Sexo": "Masculino" if Escolha == "M" else "F"
}
