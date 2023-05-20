# Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. Seu programa tem que realizar três contagens através da função criada:
# a) de 1 até 10, de 1 em 1
# b) de 10 até 0, de 2 em 2
# c) uma contagem personalizada    

from time import sleep

def contagem(c,f,p=1):
    if p < 0:
        p *= -1
        print('Passo não pode ser menor que 1, seu numero ficará positivo')
    if p == 0:
        p = 1
        print('Passo não pode ser zero, ele irá ser trocado por 1')
    if c < f:
        for c in range(c,f+1,p):
            print(c, end=" ")
            sleep(0.5)
    else:
        for c in range(c,f -1,-p):
            print(c, end=" ")
            sleep(0.5)
    print('FIM')

# contagem(1,10)
# print()
# contagem(10,-2,-2)

comeco = int(input('Escolha o começo: '))
fim = int(input('Escolha o fim: '))
passo = int(input('Escolha o passo: '))

contagem(comeco,fim,passo)