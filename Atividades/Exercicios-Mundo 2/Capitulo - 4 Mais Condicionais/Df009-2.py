import time

while True:
    try:
        while True:
            Valor_Do_Produto = float(input("Digite o valor do produto: "))
            if Valor_Do_Produto < 0:
                print("O valor do produto não pode ser negativo. Tente novamente.")
            else:
                break
    except ValueError:
        print("Entrada inválida. Por favor, digite um valor apropriado.")

    print("========LOJAS KELVYN========")
    print(" [1] à vista em dinheiro/cheque")
    print(" [2] à vista em cartão")
    print(" [3] 2x no cartão")
    print(" [4] 4x no cartão")

    try:
        while True:
            Metodo = int(input("Digite o método de pagamento: "))
            if Metodo not in [1, 2, 3, 4]:
                print("Método inválido. Por favor, escolha entre 1 e 4.")
            else:
                break
        break 
    except ValueError:
        print("Entrada inválida. Por favor, digite um número correspodente.")

if Metodo == 1:
    print(f"Você ganhou desconto de 10%, o valor ficará: {Valor_Do_Produto - (Valor_Do_Produto * 0.10):.2f}")
elif Metodo == 2:
    print(f"Você ganhou um desconto de 5%, o valor ficará {Valor_Do_Produto - (Valor_Do_Produto * 0.05):.2f}")
elif Metodo == 3:
    print(f"Você irá pagar o valor de {Valor_Do_Produto:.2f}")
else:
    Parcelas = int(input("Quantas parcelas você deseja pagar? "))
    print(f"Para {Parcelas} parcelas, você irá pagar {(Valor_Do_Produto/Parcelas) + (Valor_Do_Produto/Parcelas) * 0.20:.2f} com juros de 20% sobre cada parcela de {Valor_Do_Produto/Parcelas}")
    print(f"Sua compra de {Valor_Do_Produto:.2f} ira resultar num total de {Valor_Do_Produto + (Valor_Do_Produto * 0.20):.2f}")

