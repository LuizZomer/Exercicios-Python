import funcoes

preco = float(input('Digite um preço: '))

print(f'A metade de {preco} é {funcoes.metade(preco)}')
print(f'O dobro de {preco} é {funcoes.dobro(preco)}')
print(f'30% a mais de {preco} é {funcoes.aumentar(preco)}')
print(f'30% a menos de {preco} é {funcoes.diminuir(preco)}')