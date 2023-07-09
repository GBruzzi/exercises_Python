# condição triangulo

l1 = float(input('Digite um lado do triangulo: '))
l2 = float(input('Digite um lado do triangulo: '))
l3 = float(input('Digite um lado do triangulo: '))

if (l1 + l2) > l3 and (l2 + l3) > l1 and (l1 + l3) > l2 :
    print(f'Os lados podem formar um triângulo')

else :
    print('Os lados não podem formar um triângulo')