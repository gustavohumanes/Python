Dicionario_De_Idades = {
    "Maioridade": [],
    "Menoridade": []
}
while True:
    quantidade = int(input("Quantas pessoas deseja analisar a idade? "))
    for c in range(1, quantidade + 1):
        while True:  # Adiciona um loop interno para repetir a entrada se necessário
            try:
                idade = int(input(f"Digite a idade do indivíduo {c}: "))
                if idade > 125:
                    print("Valor incoerente, tente novamente!")
                    continue  # Reinicia apenas a entrada para esse indivíduo
                break  # Sai do loop interno se a idade for válida
            except ValueError:
                print("Insira um valor correto!")
                continue  # Reinicia a entrada no caso de erro de valor
        if idade >= 18:
            Dicionario_De_Idades['Maioridade'].append(idade)
        else:
            Dicionario_De_Idades['Menoridade'].append(idade)
    break

print(f"Da maioridade temos {Dicionario_De_Idades['Maioridade']}, num total temos {len(Dicionario_De_Idades['Maioridade'])}")
print(f"Da menoridade temos {Dicionario_De_Idades['Menoridade']}, num total temos {len(Dicionario_De_Idades['Menoridade'])}")