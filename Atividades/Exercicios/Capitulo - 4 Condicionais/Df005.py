Numero = int(input("Digite um ano: "))

if Numero % 4 == 0 and Numero % 100 != 0:
    print("Ano bissexto!")
elif Numero % 4 == 0 and Numero % 100 == 0 and Numero % 400 == 0:
    print("Bissexto!")
else:
    print("Não é bissexto!")

# Versão do chat-GPT
'''
Numero = int(input("Digite um ano: "))

if Numero % 4 == 0 and Numero % 100 != 0 or Numero % 400 == 0:
    print("Ano bissexto!")
else:
    print("Nâo é bissexto!")

'''