# Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, 
# retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.

def voto(nascimento):
    from datetime import datetime
    idade = datetime.now().year - nascimento
    if idade < 16:
        return f'Com {idade} anos: Não vota'
    elif idade < 18:
        return f'Com {idade} anos: Voto opcional'
    else:
        return f'Com {idade} anos: Voto obrigatorio'

print(voto(int(input('Ano de nascimento: '))))
