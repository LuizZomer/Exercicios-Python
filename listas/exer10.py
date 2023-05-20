# Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, 
# cadastrando tudo em uma lista composta.

from random import randint
from time import sleep

lista = []

sorteio = int(input('Quantos jogos você quer sortear? '))

for jogo in range(sorteio):
    for numero in range(6):
        r = randint(1,60)
        while r in lista:
            r = randint(1,60)
        lista.append(r)
    sleep(1)
    print(f'Jogo {jogo +1}:{sorted(lista)}')
    lista.clear()