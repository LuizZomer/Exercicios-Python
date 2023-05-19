# Exercício Python 087: Aprimore o desafio anterior, mostrando no final:  
# A) A soma de todos os valores pares digitados.   
# B) A soma dos valores da terceira coluna.   
# C) O maior valor da segunda linha.             

matriz = [[],[],[]]
coluna = 1
linha = 1
soma = soma_segunda = 0


for l in range(3):
    if l == 1:
        coluna +=1
    elif l == 2:
        coluna +=1
    primeiro = int(input(f'Escolha um numero para ({coluna},{linha}): '))
    linha +=1 
    
    for c in range(1):
        segundo = int(input(f'Escolha um numero para ({coluna},{linha}): '))
        linha+=1
        for o in range(1):
            terceiro = int(input(f'Escolha um numero para ({coluna},{linha}): '))
            linha = 1

    matriz[l].append(primeiro)  
    matriz[l].append(segundo) 
    matriz[l].append(terceiro)   

for i in matriz:
    print(i)
    for c in i:
        if c % 2==0:
            soma +=c
print(f'A soma de todos os pares é {soma}')

for i in matriz[2]:
    soma_segunda += i
print(f'A soma da terceira linha é {soma_segunda}')
print(f'O maior valor da segunda linha é {max(matriz[1])}')


