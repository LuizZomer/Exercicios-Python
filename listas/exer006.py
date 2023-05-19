# Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas,                                    guardando tudo em uma lista. No final mostre:                                                                                                  
#A)Quantas pessoas foram cadastradas.                                                                                                        B) Uma listagem com as pessoas mais pesadas.                                                                                                    
# C)listagem com as pessoas mais leves.





pessoas = []
dados = []
leves = []
pesados = []
cont = 0

while True:
    dados.append(input('Nome: '))
    dados.append(float(input('peso: ')))
    pessoas.append(dados[:])

    if len(pessoas) == 1:
        leves.append(dados[:])
        pesados.append(dados[:])
    
    else:
        if pessoas[cont][1] > pesados[0][1]:
            pesados.clear()
            pesados.append(dados[:])
        
        elif pessoas[cont][1] == pesados[0][1]:
            pesados.append(dados[:])
        
        if pessoas[cont][1] < leves[0][1]:
            leves.clear()
            leves.append(dados[:])

        elif pessoas[cont][1] == leves[0][1]:
            leves.append(dados[:])

    continuar = input('Continuar[s/n]: ').lower()
    if continuar == 'n':
        break
    cont +=1
    dados.clear()
    
print(len(pessoas))

for pessoas in leves:
    print(pessoas[0], end=',')
print('Foram os mais leves com ',leves[0][1] )

for pessoas in pesados:
    print(pessoas[0], end=',')
print('Foram os mais leves com ',pesados[0][1] )


