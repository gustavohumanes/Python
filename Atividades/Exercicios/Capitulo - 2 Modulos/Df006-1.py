import random

Quantidade_De_Alunos = int(input("Quantos alunos possui na sua sala? "))
AlunoEscolhido = random.randint(1, Quantidade_De_Alunos)

Pedro = "Pedro"
Joao = "Joao"

print(random.choice(Pedro, Joao))
print(AlunoEscolhido)