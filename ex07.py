frase = input('Digite uma frase : ').upper().strip

contador = frase.count('A')
firstA = frase.find('A') + 1
lastA = frase.rfind('A') + 1

print(f'A letra A aparece {contador} vezes')
print(f'A primeira letra A aparece na posição {firstA}')
print(f'A ultima letra A aparece na posição {lastA}')

