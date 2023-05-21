# Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
# Quantidade de notas 
# A maior nota
# A menor nota
# A média da turma
# A situação (opcional)

def notas():
    dados = {}
    geral = []
    cont = 0
    while True:
        nota = float(input('Digite a nota do aluno: '))
        geral.append(nota)
        cont+=1
        continuar = input('Continuar[S/N]? ').lower()
        if continuar == 'n':
            break
    dados['quantidade de notas'] = len(geral)
    dados['maior nota'] = max(geral)
    dados['menor nota'] = min(geral)
    dados['media'] = sum(geral)/ cont
    if dados['media'] >= 7:
        dados['situação'] = 'Boa'
    elif dados['media'] >= 5:
        dados['situação'] = 'Razoavel'
    else:
        dados['situação'] = 'Ruim'

    return dados

dados = notas()

for k,v in dados.items():
    print(f'O campo de {k} tem o valor {v}')






