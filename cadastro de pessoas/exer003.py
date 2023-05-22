from time import sleep
import esqueca

arq = 'banco.txt'

if not esqueca.arquivoexiste(arq):
    esqueca.criararquivo(arq)

def menu():
    esqueca.titulo('Menu pricipal')
    print('1 - Ver pessoas cadastradas\n2 - Cadastrar nova pessoa\n3 - Sair do sistema')
    opcaotxt = input('Sua opções: ')
    try:
        opcao = int(opcaotxt)
    except ValueError:
        print('Essa opção é invalida')
        sleep(1)
        menu()
        
    
    match opcao:
        case 1:
            esqueca.titulo('Pessoas cadastradas')
            esqueca.lerarquivos('banco.txt')
            menu()
        case 2:
            esqueca.titulo('Cadastro de pessoas')
            nome = input('Nome: ')
            idade = esqueca.leiaInt(input('Digite a idade: '))
            esqueca.cadastrar(arq,nome,idade,)
            menu()
        case 3:
            print('Saindo do programa...')
        case _:
            print('Opção inexistente')
            sleep(1)
            menu()
    


menu()