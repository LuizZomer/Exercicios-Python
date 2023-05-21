# Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: 
# o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, 
# mesmo que algum dado não tenha sido informado corretamente.

def status(n='desconhecido',g=0):
    print(f'O jogador {n} marcou {g} gols')

nome = input('Nome do jogador: ')
gols = str(input('Quantos gols ele fez? '))

if gols.isnumeric():
    int(gols)
else:
    gols = 0

if nome.strip() == '':
    status(g=gols)
else:
    status(nome,gols)

