# Aprimore o desafio 93 para que ele funcione com vários jogadores, 
# incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.

jogadores = []
status = dict()
gols = []


while True:
    status['nome'] = input('Nome do jogador: ')
    partidas = int(input(f'Quantas partidas {status["nome"]} jogou: '))
    for p in range(partidas):
        gols.append(int(input(f'Gols na partida {p+1}: ')))

    status['gols'] = gols[:] 
    status['total'] = sum(gols)
    jogadores.append(status.copy())
    gols.clear()
    continuar = input('Deseja continuar[S/N]? ').lower()[0]
    if continuar == 'n':
         break

print('-='*30)
print('cod   Nome   Gols       total')
for i,v in enumerate(jogadores):
    print(f'{i}  {v["nome"]}    {v["gols"]}    {v["total"]}')



while True:
    escolha = int(input('Escolha um jogador para detalhar[999 para]: '))
    
    if escolha > len(jogadores):
        print('Jogador inexistente')
    if escolha == 999:
        break
    else:
        print()
        print(f'Levantamento do {jogadores[escolha]["nome"]}:')
        for i,g in enumerate(jogadores[escolha]['gols']):
            print(f'    No jogo {i+1} fez {g} gols')

print('Encerrando')
