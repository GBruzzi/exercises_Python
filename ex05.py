#Aluguel de carros

dias = int(input('Quantos dias alugados ? ')) 
d = float(input('Quantos km rodados ? ')) 

p = (dias * 60) + (d * 0.15)

print(f'O preço a ser pago é {p}')