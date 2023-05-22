import funcoes

preco = float(input('Digite um preço: '))

print(f'A metade de {funcoes.moeda(preco)} é {funcoes.metade(preco, True)}')
print(f'O dobro de {funcoes.moeda(preco)} é {funcoes.dobro(preco, True)}')
print(f'30% a mais de {funcoes.moeda(preco)} é {funcoes.aumentar(preco, True)}')
print(f'30% a menos de {funcoes.moeda(preco)} é {funcoes.diminuir(preco, True)}')