nome = str(input("Digite o nome de uma cidade: ")).upper()

if("SILVA" in nome.split()):
    print(f"Olá, está cidade possui 'SILVA' no nome!")
else:
    print(f"Está é a cidade {nome.title()}")