Valor_Da_Casa = float(input("Digite o valor da casa: "))
Salario_Do_Comprador = float(input("Digite o salário do comprador em meses: "))
Anos = float(input("Digite, em anos, o tempo que pretende levar para pagar: "))

Valor_Da_Prestação_Mensal = (Valor_Da_Casa/Anos)/12
Porcentagem_Do_Salario_Do_Comprador = Salario_Do_Comprador*0.30

print(f"O Valor_Da_Prestação_Mensal é: {Valor_Da_Prestação_Mensal}")
print(f"30% Do Salario Do Comprador é: {Porcentagem_Do_Salario_Do_Comprador}")

if Valor_Da_Prestação_Mensal > Porcentagem_Do_Salario_Do_Comprador:
    print("Você não é elegível para a prestação!")
else:
    print("Você é elegível para a prestação!")