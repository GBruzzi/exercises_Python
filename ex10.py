#custo viagem

km = int(input('Qual a distancia da sua viagem ?'))
price = ''

if km > 200 :
    price = km * 45

else :
    price = km * 50

print(f'Para uma viagem de {km} km , o preço será ${price}')