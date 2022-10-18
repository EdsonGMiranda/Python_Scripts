# Exercício Python 10: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira
# e mostre quantos dólares ela pode comprar.

n = float(input('Quanto você tem na carteira? R$'))
d = 5.15
print('Com {:.2f} você pode comprar ${:.2f} de dolares'.format(n, (n/d)))
