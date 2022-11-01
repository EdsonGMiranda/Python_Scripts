# Exercício Python 108: Adapte o código do desafio #107, criando uma função adicional chamada moeda()
# que consiga mostrar os números como um valor monetário formatado.

import moeda

n = float(input('Digite o preço: R$'))
met = moeda.metade(n)
tax = 40
au = moeda.aumentar(n, tax)
di = moeda.diminuir(n, tax)
do = moeda.dobro(n)


print(f'A metade de {moeda.moeda(n)} é {moeda.moeda(met)}')
print(f'O dobro de {moeda.moeda(n)} é {moeda.moeda(do)}')
print(f'Aumentando {tax}% de  {moeda.moeda(n)} é {moeda.moeda(au)}')
print(f'Diminuindo {tax}% de  {moeda.moeda(n)} é {moeda.moeda(di)}')



