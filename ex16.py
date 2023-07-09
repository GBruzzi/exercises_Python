# calc soma ímpar

soma = 0

for c in range(1,500,2) :
    if c % 3 == 0 :
        soma += c

print(f'A soma dos números ímpares divisiveis por 3 entre 1 e 500 é {soma}')        