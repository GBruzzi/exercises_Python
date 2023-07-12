# Cadastro jogador futebol

jogador = {}
partidas = []
jogador['nome'] = str(input('Nome : '))
tot = int(input(f'Quantas partidas o {jogador["nome"]} fez? '))

for c in range(0,tot) :
    quant = 0
    partidas.append(int(input(f'Quantos gols na partida {c} ? ')))
    
jogador['gols'] = partidas
jogador['total'] = sum(partidas)
print(jogador)
