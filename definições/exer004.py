# Faça um programa que tenha uma função chamada maior(),
# que receba vários parâmetros com valores inteiros. 
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

def maior(*args):
    maior = max(args)
    print(f'Entre os valores:',end=" ")
    for c in args:
        print(c,end=" ")
    print()
    print(f'o maior numero é o {maior}')

#Codigo principal

lista = []

while True:
    lista.append(int(input('Digite um numero: ')))
    continuar = input('Deseja continuar[S/N]? ').lower()
    if continuar == 'n':
        break

maior(*lista)


