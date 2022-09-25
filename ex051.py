# Exercício Python 51: Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
# No final, mostre os 10 primeiros termos dessa progressão.
print('-=' *10)
print('10 TERMOS DE UMA PA')
print('-=' *10)
a1 = int(input('Entre com o primeiro termo da PA: '))
r = int(input('Entre com a razão de uma PA: '))
a10 = a1 + (10 - 1) * r
for i in range(a1, a10 + r, r):
    print('{} '.format(i), end='-> ')
print('...')
