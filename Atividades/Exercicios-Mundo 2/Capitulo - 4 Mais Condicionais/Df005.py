Notas = []

for Number in range(2):
    Valor = float(input("Digite a nota do aluno: "))
    Notas.append(Valor)

Media_Do_Aluno = (Notas[0] + Notas[1])/2

if Media_Do_Aluno < 5:
    print("Reprovado")
elif Media_Do_Aluno > 5 and Media_Do_Aluno < 6.9:
    print("Recuperação")
else:
    print("Aprovado!")