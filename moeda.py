# aumentar(), diminuir(), dobro() e metade()


def aumentar(n, tax=10, formata=False):
    a = n + (n * (tax/100))
    if formata:
        return moeda(a)
    else:
        return a


def diminuir(n, tax=10, formata=False):
    d = n - (n * (tax/100))
    if formata:
        return moeda(d)
    else:
        return d


def dobro(n, formata=False):
    d = n * 2
    if formata:
        return moeda(d)
    else:
        return d


def metade(n, formata=False):
    m = n / 2
    return m if not formata else moeda(m)


def moeda(n=0, moeda='R$'):
    return f' {moeda} {n:.2f}'.replace('.', ',')


def resumo(n, red=12, aum=10):
    met = metade(n, formata=True)
    au = aumentar(n, aum, formata=True)
    di = diminuir(n, red, formata=True)
    do = dobro(n, formata=True)

    print(f'-' * 35)
    print(f'RESUMO DO VALOR'.center(30))
    print(f'-' * 35)
    print(f'Preço Analisado: \t{moeda(n)}')
    print(f'Dobro do Preço: \t{do}')
    print(f'Metade do Preço: \t{met}')
    print(f'{aum}% de aumento: \t{au}')
    print(f'{red}% de redução: \t{di}')






