# Menu opções

maior = 0
menor = 100000000000000000


n1 = int(input('Primeiro valor : '))
n2 = int(input('Segundo valor : '))

while True :
    escolha = 0
    print('-------------------------')
    print('Olhe as opções abaixo :')
    print('[1] Somar       ')
    print('[2] Multiplicar        ')
    print('[3] Maior        ')
    print('[4] Novos números        ')
    print('[5] Sair do programa        ')
    escolha = int(input('Qual sua opção ? '))
    if escolha == 1 :
        print(f'A soma entre {n1} e {n2} é igual a {n1 + n2}')
    elif escolha == 2 :
        print(f'A multiplicação entre {n2} e {n1} é igual a {n2 * n1}')
    elif escolha == 3 :
        if n1 > n2 :
            print(f'{n1} é o maior valor')
        elif n2 > n1 :
            print(f'{n2} é o maior valor')
        else :
            print(f'{n1} e {n2} são iguais')  
    elif escolha == 4 :
        n1 = int(input('Primeiro valor : '))
        n2 = int(input('Segundo valor : '))         
    elif escolha == 5 :
        break
    else :
        print('Por favor, digite uma opção válida')
print('Obrigado por participar')    