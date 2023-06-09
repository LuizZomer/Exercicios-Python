# Faça um mini-sistema que utilize o Interactive Help do Python.
# O usuário vai digitar o comando e o manual vai aparecer. 
# Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará. Importante: use cores.

c = ('\033[m', #sem cor
     '\033[0;30;41m', #Vermelho
     '\033[0;30;42m', #verde
     '\033[0;30;43m', #amarelo
     '\033[0;30;44m', #azul
     '\033[0;30;45m', #roxo
     '\033[7;30m' #branco
     )

def ajuda(com):
    titulo(f'Acessando o manual do comando \'{com}\'',4)
    print(c[6], end='')
    help(com)
    print(c[0],end='')


def titulo(msg,cor=0):
    tam = len(msg) +4
    print(c[cor], end='')
    print('~'*tam)
    print(f'  {msg}')
    print('~'*tam)
    print(c[0],end='')

comando = ''
while True:
    titulo('SISTEMA DE AJUDA PyHELP', 2)
    comando = str(input('Função ou biblioteca >'))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('Até logo!',1)