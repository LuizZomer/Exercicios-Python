def resumo(n):
    def metade(num):
        x = num / 2
        print(f'A metade de {moeda(num)} é moeda {moeda(x)}')

    def dobro(num):
        x = num *2
        print(f'O dobro de {moeda(num)} é moeda {moeda(x)}')

    def aumentar(num, format = False):
        x = num * 1.3
        print(f'30% a mais de {num} é {moeda(x)}')

    def diminuir(num,formato = False):
        x = num * 0.7
        print(f'30% a mais de {num} é {moeda(x)}')

    def moeda(preco, moeda='R$'):
        return f'{moeda}{preco:.2f}'.replace('.',',')

    metade(n)
    dobro(n)
    aumentar(n)
    diminuir(n)