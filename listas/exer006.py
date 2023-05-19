pessoas = []
dados = []
leves = []
pesadas = []



while True:
    dados.append(input('Nome: '))
    dados.append(float(input('peso: ')))
    pessoas.append(dados[:])
    dados.clear()
    continuar = input('Deseja continuar[S/N]: ').lower()
    if continuar == 'n':
        break

maior = pessoas[0][1]
menor = pessoas[0][1]

for pessoa in pessoas:
  
    if pessoa[1] >= maior:
        maior = pessoa[1]
        pesadas.append(pessoa[0])
        
    
    if pessoa[1] <= menor:
        menor = pessoa[1]
        leves.append(pessoa[0]) 
        


print(f'Foram registrados {len(pessoas)} pessoas')
for leve in leves:
    print(leve, end=",")
print(f'Foram os mais leves com {menor} kilos')
for p in pesadas:
    print(p,end=",")
print(f'Esse foram os mais pesados com {maior} kilos')


