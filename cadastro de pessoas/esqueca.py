

def arquivoexiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criararquivo(nome):
    try:
        a = open(nome,'wt+')
        a.close()
    except:
        print('Houve um erro na criação do arquivo')
    else:
        print(f'Arquivo {nome} Criado com sucesso')


def lerarquivos(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo')
    else:
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n','')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close()


def linha():
    print('-'*40)


def titulo(msg):
    linha()
    print(msg.center(40))
    linha()


def leiaInt(num):
    try:
        n = int(num)
        return n
    except:
        while True:
            print('Erro')
            try:
                n = input('Digite um numero inteiro para a idade: ')
                n = int(n)
                return n
            except:
                print()


def cadastrar(arq, nome='desconhecido',idade=0):
    try:
        a = open(arq, 'at')
    except:
        print('Houve um erro na abertura')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um erro ao digitar os dados')
        else:
            print(f'Novo registro {nome} adicionado')
            a.close()
