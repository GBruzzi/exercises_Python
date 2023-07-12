# Extraindo dados de uma list

lista = []
c = 0
testeCinco = False
while True :
    n = int(input('Digite um valor : '))
    lista.append(n)
    c += 1
    if n == 5 :
        testeCinco = True
    escolha = input('Quer continuar ? [S/N]' ).upper()
    if escolha in 'Nn' :
        break
    while escolha not in 'SsNn' :
        escolha = input('Quer continuar ? [S/N]' ).upper()
lista.sort(reverse=True)
print(f'Os valores digitados foram {lista}')
print(f'Os valores em ordem decrescente são {lista}')
if testeCinco :
    print(f'O valor cinco FAZ parte da lista')
else :
    print('O valor cinco NÃO FAZ parte da lista')    
print('Obrigado por participar')


