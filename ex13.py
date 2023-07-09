# Alistamento Militar

date = int(input('Informe seu ano de nascimento : '))

idade = 2023 - date
alistar = 18 - idade

if idade < 18 :
    print(f'Quem nasce em {date} tem {idade} anos e ainda faltam {alistar} ano para se alistar')
elif idade == 18 :
    print(f'Quem nasce em {date} tem {idade} anos e está na hora de alistar !')
else :
    print(f'Quem nasce em {date} tem {idade} anos e ja passou da hora de se alistar !')