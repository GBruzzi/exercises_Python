# analisando dados de um grupo

print('Cadastre uma pessoa')
print('--------=---------')

maior18 = 0
quantH = 0
teste = 'S'
mulher20 = 0

while teste in 'S':
    idade = int(input('Idade : '))
    if idade > 18 :
        maior18 += 1
    sexo = input('Sexo [H/M] : ').upper()
    if sexo == 'M' and idade < 20 :
        mulher20 += 1
    while sexo not in 'HM' :
        sexo = input('Sexo [H/M] : ').upper()
    if sexo == 'H' :
        quantH += 1
    teste = input('Quer continuar [S/N] ? ').upper()
    if teste == 'N':
        break
    while teste != 'S' :
        teste = input('Quer continuar [S/N] ? ').upper()
    print('------=--------')

print('---------=--------')
print(f'Temos ao todo {maior18} pessoas com mais de 18 anos')
print(f'Temos ao todo {quantH} homens cadastrados')
print(f'Temos ao todo {mulher20} mulheres com menos de 20 anos')
print('Obrigado por participar ')    