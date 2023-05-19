# Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única 
# que mantenha separados os valores pares e ímpares. No final,
# mostre os valores pares e ímpares em ordem crescente.

numeros = [[],[]]

for c in range(7):
    numero = int(input('digite um numero: '))
    if numero % 2 == 0:
        numeros[0].append(numero)
    else:
        numeros[1].append(numero)

for i in numeros:
    print(i)