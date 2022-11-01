# Exercício Python 107: Crie um módulo chamado moeda.py que tenha
# as funções incorporadas aumentar(), diminuir(), dobro() e metade().
# Faça também um programa que importe esse módulo e use algumas dessas funções.

import moeda

n = float(input('Digite o preço: R$'))
met = moeda.metade(n)
tax = 40
au = moeda.aumentar(n, tax)
di = moeda.diminuir(n, tax)
do = moeda.dobro(n)


print(f'A metade de R${n:.2f} é R${met}')
print(f'O dobro de R${n:.2f} é R${do}')
print(f'Aumentando {tax}% de  R${n:.2f} é R${au:.2f}')
print(f'Diminuindo {tax}% de  R${n:.2f} é R${di:.2f}')
