# Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de tipo inválido. 
# Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.

def leiaInt():
    tipo = 'inteiro'
    while True:
        if teste(int,tipo):
            break


def leiaFloat():
    tipo = 'real'
    while True:
        if teste(float,tipo):
            break
    
    
def teste(tipo,enum):
    try:
        num = input(f'Digite um numero {enum}: ')
        tipo(num)
    except (ValueError, TypeError):
        print('Valor digitado não está correto')
        return False
    except KeyboardInterrupt:
        print('O usuario preferiu interromper')
        num = 0
        print(f'Você digitou o numero {num}')
    else:
        print(f'Você digitou o numero {num}')
        return True


leiaInt()
leiaFloat()


