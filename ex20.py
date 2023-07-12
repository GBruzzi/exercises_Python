# Tuplas com time de futebol

Classificacao = ('Cruzeiro', 'Atletico', 'Palmeiras', 'Flamengo', 'Grêmio', 'Botafogo')
primeiros = Classificacao[:2]
ultimos = Classificacao[4:]
ordenada = sorted(Classificacao)

print(f'A tabela geral é {Classificacao}')
print('----------------------')
print(f'Os 2 últimos são {ultimos}')
print('-----------------------')
print(f'Os 2 primeiros são {primeiros}')
print('---------------')
print(f'A lista ordenada por ordem alfábetica é {ordenada}')
