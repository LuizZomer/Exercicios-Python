# Crie um programa que tenha a função leiaInt(), 
# que vai funcionar de forma semelhante ‘a função input() do Python, 
# só que fazendo a validação para aceitar apenas um valor numérico. Ex: n = leiaInt(‘Digite um n: ‘)

def leiaInt():
    inteiro = False
    while True:
        num = input('Digite um numero: ')

        if num.isnumeric():
            numero = int(num) 
            inteiro = True
        else:
            print(f'ERRO!Digite um valor valido')
        if inteiro:
            return numero


num = leiaInt()

print(f'Você digitou o numero {num}')