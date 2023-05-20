# Faça um programa que tenha uma função chamada área(),
# que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.

def area(l,c):
    terreno = l * c
    print(f'A área de um terreno {l}x{c} é de {terreno}m²')

#Programa principal
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))

area(l,c)