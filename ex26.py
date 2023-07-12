# cadastro digital

trabalhador = {}

trabalhador['nome'] = str(input('Digite um nome : '))
trabalhador['ano'] = int(input('Ano de nascimento : '))
trabalhador['ctps'] = int(input('Carteira de trabalho (0 não tem ) : '))
if trabalhador['ctps'] != 0 :
    trabalhador['contra'] = int(input('Ano de contratação : '))
    trabalhador['gold'] = float(input('Salário : '))

idade = 2023 - trabalhador['ano']
aposentadoria = idade + 30

print(f'O nome é {trabalhador["nome"]}')
print(f'A idade é {idade} anos')
print(f'Vai aposentar com {aposentadoria} anos')