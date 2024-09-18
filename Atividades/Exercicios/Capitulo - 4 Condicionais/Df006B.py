n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite um último número: '))

lista = [n1, n2, n3]
lista.sort() #o método .sort() ordena os números da lista em ordem crescente, tornando  o programa mais compacto

print(f'O maior número é {lista[2]} e o menor é {lista[0]}')