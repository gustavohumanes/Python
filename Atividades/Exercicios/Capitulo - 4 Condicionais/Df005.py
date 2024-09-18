import datetime

Numero = int(input("Digite um ano, caso queira o ano atual, digite 0: "))

if Numero == 0:
    ano = datetime.date.today().year

if Numero % 4 == 0 and Numero % 100 != 0 or Numero % 400 == 0:
    print("Ano bissexto!")
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