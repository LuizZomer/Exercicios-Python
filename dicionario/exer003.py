# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário.
# Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. 
# Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

from datetime import datetime

funcionario = {}
ano = datetime.now().year

funcionario['nome'] = input('Nome do funcionario: ')
nascimento = int(input('Ano de nascimento: '))
funcionario['idade'] = ano - nascimento
funcionario['carteira'] = int(input('Carteira de trabalho[0 não tem]: '))

if funcionario['carteira'] == 0:
    for k,v in funcionario.items():
        print(f'{k} tem o valor {v}')
else:
    funcionario['contratacao'] = int(input('Ano de contratação: '))
    funcionario['salario'] = float(input('Salário: R$'))
    funcionario['aposentadoria'] = funcionario['idade'] +((funcionario['contratacao'] + 35) - ano)
    for k,v in funcionario.items():
        print(f'{k} tem o valor {v}')
