frase = "  Meu pau tem 15Cm  "

print(frase.replace("15cm", "1cm" )) # Substitui os 15cm por 1cm

print(frase.upper()) # Deixa maiúsuclo

print(frase.lower()) # Deixa minúsculo

print(frase.capitalize()) # Deixa a apenas a primeira letra maiúscula, e o resto fica minúscula

print(frase.title()) # Deixa a apenas as letras após espaços, maiúsculas

print(frase.strip()) # Tira os espaços inúteis

print(frase.rstrip()) # Tira os espaços inúteis apenas do final, os do começo ficam
print(frase.lstrip()) # Tira os espaços inúteis apenas do começo, os do final ficam

print(frase.split()) # Gera uma lista de uma string

Sla = frase.split()
print('-'.join(Sla)) # Gera uma lista de uma string