# maior e menor valor

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite um valor: '))
n3 = int(input('Digite um valor: '))

maior = 0
menor = 1000000

if n1 > n2:
    maior = n1
    menor = n2
else:
    maior = n2
    menor = n1

if n3 > maior:
    maior = n3
elif n3 < menor:
    menor = n3

print(f'O maior valor é {maior} e o menor valor é {menor}.')

    