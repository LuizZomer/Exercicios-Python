# Faça um programa que tenha uma função chamada escreva(),
# que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.      

def texto(p):
    print('~'*(len(p) + 4))
    print(f'  {p}')
    print('~'*(len(p) + 4))

palavra = input('Escreva algo: ')
texto(palavra)