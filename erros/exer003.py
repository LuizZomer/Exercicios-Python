from time import sleep

def menu():
    titulo('Menu pricipal')
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
            print('Ver pessoas')
        case 2:
            print('Cadastrar Pessoas')
        case 3:
            print('Saindo do programa')
        case _:
            print('Opção inexistente')
            sleep(1)
            menu()
    

def linha():
    print('-'*40)

def titulo(msg):
    linha()
    print(msg.center(40))
    linha()

menu()