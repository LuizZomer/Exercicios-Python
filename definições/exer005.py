#  Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.
from random import randint

def sorteia():
    numeros = []
    for c in range(5):
        numeros.append(randint(1,10))
    print(f'Os numeros sorteados foram: {numeros}')
    def somapar(lista):
        soma = 0
        for c in lista:
            if c % 2 == 0:
                soma += c
        print(f'O resultado da soma dos numeros pares foi:{soma}')
    somapar(numeros)

sorteia()