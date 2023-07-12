# Analise dados Tuple


n = (int(input('Digite um número : ')),
     int(input('Digite um número : ')),  
     int(input('Digite um número : ')), 
     int(input('Digite um número : ')))

print(f'Você digitou os valores {n}')
print(f'O número 9 apareceu {n.count(9)} vezes')
if 3 in n :
    print(f'O primeiro valor 3 foi digitado na posição {n.index(3) + 1}')
else :
    print('O valor 3 não foi digitado')    

pares = 0
for c in n :
    if c % 2 == 0 :
        pares = pares + 1
print(f'Ao todo foram digitados {pares} números pares')


