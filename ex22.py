# maior e menor valor de uma lista


maior = 0
posmaior = ''

lista = []

for c in range(0,5) :
    n = int(input(f'Digite um valor para a posição {c} : '))
    lista.append(n)
    if n > maior :
        maior = n
        posmaior = lista.index(n)

print(f'Os valores digitados foram : {lista}')
print(f'O maior valor digitado foi o {maior} na posição {posmaior}')