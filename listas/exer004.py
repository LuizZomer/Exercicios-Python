# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, 
# crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, 
# respectivamente. Ao final, mostre o conteúdo das três listas geradas.

lista = []

while True:
    numero = int(input('Digite um numero: '))
    lista.append(numero)
    escolha = input('Continuar[s/n]: ').lower()
    if 'n' in escolha:
        break
lista_pares = []
lista_impares = []

for num in lista:
    if num%2==0:
        lista_pares.append(num)
    else:
        lista_impares.append(num)

print('A lista normal ',lista)
print('A lista só de pares',lista_pares)
print('A lista só de impares',lista_impares)