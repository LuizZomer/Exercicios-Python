# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em listas. 
# No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

alunos = list()
geral = []
notas = []

while True:
    alunos.append(input('Nome do aluno: '))
    alunos.append(float(input('nota 1: ')))
    alunos.append(float(input('Nota 2: ')))
    notas.append(alunos[:])
    alunos.append((alunos[1] + alunos[2]) / 2)
    geral.append(alunos[::3])
    alunos.clear()

    continuar = input('deseja continuar[S/N]? ').lower()
    if continuar == 'n':
        break

print('nº|aluno|média')
for index,nome in enumerate(geral):
    print(index, nome) 

while True:
    selecao = int(input('Selecione um aluno pelo nº[999 cancela]: '))
    if selecao == 999:
        break
    if selecao > len(notas) -1:
        print('Numero de aluno inexistente')
    else:
        print('Aluno |Nota 1|Nota 2')
        print(notas[selecao])


