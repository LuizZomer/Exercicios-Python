# Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

status = dict()
gols = []

status['nome'] = input('Nome do jogador: ')
partidas = int(input(f'Quantas partidas {status["nome"]} jogou: '))
for p in range(partidas):
     gols.append(int(input(f'Gols na partida {p+1}: ')))

status['gols'] = gols[:] 
status['total'] = sum(gols)

print('-='*30)

print(status)

print('-='*30)

for k,v in status.items():
     print(f'O campo {k} tem o valor {v}')

print('-='*30)

print(f'O jogador {status["nome"]} jogos {partidas} partidas.')
for i,v in enumerate(status['gols']):
     print(f'  => Na partida {i+1}, fez {v} gols')