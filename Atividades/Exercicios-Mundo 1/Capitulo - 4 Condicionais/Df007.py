SalarioDoVagabundo = float(input('Digite o salario desse caralho: '))

if SalarioDoVagabundo > 1250.0:
    print(f"O salario do menino agora é {SalarioDoVagabundo*0.10 + SalarioDoVagabundo:.2f}")
else:
    print(f"O salario do meino agora é {SalarioDoVagabundo*0.15 + SalarioDoVagabundo:.2f}")