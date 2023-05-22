

def metade(num, format = False):
    num /= 2
    return num if format is False else moeda(num)

def dobro(num, format = False):
    num *= 2
    return num if format is False else moeda(num)

def aumentar(num, format = False):
    num = num * 1.3
    return num if format is False else moeda(num)

def diminuir(num,formato = False):
    num = num * 0.7
    return num if formato is False else moeda(num)

def moeda(preco, moeda='R$'):
    return f'{moeda}{preco:.2f}'.replace('.',',')