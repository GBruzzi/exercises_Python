# Analisador de um grupo

soma = 0
quantM = 0

idadeHomemVelho = 0
nomeHomem = ''



for c in range(0,4) :
    nome = input('Nome: ')
    idade = int(input('Idade : '))
    soma += idade
    sexo = input('Sexo [H/M] : ').upper()
    if sexo == 'H' and idade >  idadeHomemVelho :
        idadeHomemVelho = idade
        nomeHomem = nome
    if sexo == 'M' and idade < 21 :
        quantM += 1    
    print('--------------------------------')

media = soma / 4

print(f'A média de idade do grupo é {media:.2F}')
print(f'O homem mais velho se chama {nomeHomem} e tem {idadeHomemVelho} anos')
print(f'Ao todo , são {quantM} mulheres com menos de 20 anos')