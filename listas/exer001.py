# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

lista = []

for v in range(5):
    numero = float(input('Digite um numero: '))
    lista.append(numero)

print(f'O maior numero é {max(lista)} e está na posição {lista.index(max(lista))}')
print(f'O menor numero é {min(lista)} e está na posição {lista.index(min(lista))}')