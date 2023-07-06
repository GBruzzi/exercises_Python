#analisando nomes

nome = input('Digite seu nome completo : ').strip()

masc = nome.upper()
min = nome.lower()
tam = (len(nome) - nome.count(' '))

print(f'Seu nome em maisculo é {masc} e em minusculo é {min}')
print(f'Além disso ele também tem {tam} letras')