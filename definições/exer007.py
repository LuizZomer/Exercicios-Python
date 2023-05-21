# Crie um programa que tenha uma função fatorial() que receba dois parâmetros: 
# o primeiro que indique o número a calcular e outro chamado show, 
# que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.

def fatorial(num, show=True):
    f = 1
    if show:
        for n in range(num,0,-1):
            f *=n
            if n > 1:
                print(n, end=' x ')
            else:
                print('1 = ', end='')
        print(f)

    else:
        for n in range(num,0,-1):
            f *=n
        print(f'O valor do fatorial de {num} é {f}')
        
            

fat = int(input('Numero para fazer o fatorial: '))
show = input('Deseja mostrar a conta na tela[S/N]? ').lower()
if show == 'n':
    show = False

fatorial(fat, show)