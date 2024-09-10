Frase = str(input("Digite uma frase: "))

print(f"A letra 'a' aparece na frase {Frase.count("a")} vezes!")
print(f"Aparece a primeira vez no espaço {int(Frase.find("a")) + 1} da string")
print(f"Aparece na última vez no espaço {int(Frase.rfind("a")) + 1} da string")