def metade(preço=0):
    res =  preço / 2
    return res

def dobro(preço=0):
    res = preço * 2
    return res

def aumentar(preço=0, porc=0):
    res =  preço * (100 + porc) / 100
    return res

def diminuir(preço=0, porc=0):
    res = preço * (100 - porc) / 100
    return res

def moeda(preço=0, moeda='R$'):
    return f'{moeda}{preço:.2f}'.replace('.',',')