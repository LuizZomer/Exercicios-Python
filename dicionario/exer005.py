# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. 
# No final, mostre: 
# A) Quantas pessoas foram cadastradas 
# B) A média de idade 
# C) Uma lista com as mulheres
# D) Uma lista de pessoas com idade acima da média

pessoas = []
dados = {}
mulheres = []
acima_idade = []
soma = 0

while True:
    dados['nome'] = input('Nome: ')
    dados['idade'] = int(input('Idade: '))
    while True:
        dados['sexo'] = input('Sexo[F/M]: ').lower()[0]
        if dados['sexo'] in 'mf':
            break
        print('ERRO!Digite m ou ')
    pessoas.append(dados.copy())
    continuar = input('deseja continuar[S/N]? ').lower()[0]
    if continuar == 'n':
        break
    if continuar != 'n' and continuar != 's':
        while continuar != 'n' and continuar != 's':
            print('Opção não existente.')
            continuar = input('deseja continuar[S/N]? ').lower()

print(f'{len(pessoas)} pessoas foram cadastradas')

for p in pessoas:
    soma += p['idade']
    if 'f'in p['sexo']:
        mulheres.append(p['nome'])

media = soma/len(pessoas)
print(media)
print(f'As mulheres cadastradas:{mulheres}')

for p in pessoas:
    if p['idade'] > media:
        acima_idade.append(p['nome'])
print(f'As pessoa que são acima da media de idade:{acima_idade}')




