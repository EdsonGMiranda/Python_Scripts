# Exercício Python 109: Modifique as funções que form criadas no desafio 107 para que elas aceitem um parâmetro a mais,
# informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.

import moeda

n = float(input('Digite o preço: R$ '))
met = moeda.metade(n, formata=True)
tax = 22
au = moeda.aumentar(n, tax, formata=True)
di = moeda.diminuir(n, tax, formata=True)
do = moeda.dobro(n, formata=True)


print(f'A metade de {moeda.moeda(n)} é {met}')
print(f'O dobro de {moeda.moeda(n)} é {do}')
print(f'Aumentando {tax}% de  {n} é {au}')
print(f'Diminuindo {tax}% de  {n} é {di}')