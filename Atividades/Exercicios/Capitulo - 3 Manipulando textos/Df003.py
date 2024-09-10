Nome = str(input("Digite seu nome: ")).strip()

print(f"Seu nome é {Nome.upper()}")
print(f"Seu nome é {Nome.lower()}")
print(f"Seu nome possui {len(Nome.replace(" ", ""))} letras!")
print(f"Seu primeiro nome é {Nome.split()[0]} e ele tem {len(Nome.split()[0])} letras")