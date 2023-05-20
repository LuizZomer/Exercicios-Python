# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
# No final, mostre o conteúdo da estrutura na tela.

geral = []
dados = {}


while True:
    dados['nome'] = input('Nome: ')
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    dados['media'] = (nota1 + nota2) / 2
    if dados['media'] > 7:
        dados['situacao'] = 'Aprovado'
    else:
        dados['situacao'] = 'Reprovado'
    geral.append(dados.copy())

    continuar = input('Deseja continuar[S/N]? ').lower()
    if continuar == 'n':
        break

for i in geral:
    print(f'O {i["nome"]} tirou média {i["media"]} e foi {i["situacao"]} ')



