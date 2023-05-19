numeros = [[],[]]

for c in range(7):
    numero = int(input('digite um numero: '))
    if numero % 2 == 0:
        numeros[0].append(numero)
    else:
        numeros[1].append(numero)

for i in numeros:
    print(i)