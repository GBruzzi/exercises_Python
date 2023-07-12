# Dict Python

aluno = {}

aluno['nome'] = str(input('Digite o nome : '))
aluno['média'] = float(input('Digite a média : '))


if aluno['média'] > 60 :
    print('O aluno foi aprovado !')
    aluno['res'] = 'OK'
else :
    print('O aluno foi reprovado :(')
    aluno['res'] = 'BAD'
print(aluno)