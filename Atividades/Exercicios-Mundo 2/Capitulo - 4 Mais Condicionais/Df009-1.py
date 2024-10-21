#Código feito por Kelvyn

Valor_Do_Produto = float(input("Digite o valor do produto: "))

print("1- Dinheiro/Cheque")
print("2- Cartão de crédito em X1")
print("3- Cartão de crédito em X2")
print("4- Cartão de crédito em X3 ou mais")

Metodo = int(input("Digite o método de pagamento:"))
Valor_Com_Desconto = None
Metodo_Usado = ""

if Metodo == 1:
    Metodo_Usado = "Dinheiro/Cheque"
    Valor_Com_Desconto = Valor_Do_Produto - (Valor_Do_Produto * 0.10)
elif Metodo == 2:
    Metodo_Usado = "Cartão de crédito em X1"
    Valor_Com_Desconto = Valor_Do_Produto - (Valor_Do_Produto * 0.05)
elif Metodo == 3:
    Metodo_Usado = "Cartão de crédito em X2"
    Valor_Com_Desconto = Valor_Do_Produto
elif Metodo == 4:
    Metodo_Usado = "Cartão de crédito em X3 ou mais"
    Valor_Com_Desconto = Valor_Do_Produto + (Valor_Do_Produto * 0.20)
else:
    print("Método invalido")

if Valor_Com_Desconto is not None:
    print(f"Com o método {Metodo_Usado} de pagamento, você terá que pagar {Valor_Com_Desconto:.2f}")