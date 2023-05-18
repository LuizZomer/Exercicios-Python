# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. 
# Caso o número já exista lá dentro, ele não será adicionado. 
# No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

lista = list()

while True:
    numero = float(input('Digite um numero: '))
    if numero in lista:
        print('Esse valor já está na lista')
    else:
        lista.append(numero)
    continuar = input('Continuar[S/N]: ').lower()
    if continuar == 'n':
        break

print(sorted(lista))