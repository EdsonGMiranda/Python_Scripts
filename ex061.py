# Exercício Python 61: Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA,
# mostrando os 10 primeiros termos da progressão usando a estrutura while.

print('-=' *10)
print('10 TERMOS DE UMA PA')
print('-=' *10)

a1 = int(input('Entre com o primeiro termo da PA: '))
r = int(input('Entre com a razão de uma PA: '))
a10 = a1 + (10 - 1) * r
count = 0
p = a1
while count <= 10:
    print('{} '.format(p), end=' -> ')
    p += r
    count += 1
print('...')