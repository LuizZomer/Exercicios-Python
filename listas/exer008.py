matriz = [[],[],[]]
coluna = 1
linha = 1

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



    