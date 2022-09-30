# Exercício Python 63: Escreva um programa que leia um número N inteiro qualquer e mostre na tela os
# N primeiros elementos de uma Sequência de Fibonacci. Exemplo:
# 0 – 1 – 1 – 2 – 3 – 5 – 8

n = int(input('Entre com numero de termos que deseja ver da sequencia de fibonacci: '))
f1 = 0
f2 = 1
cont = 3
print('{}-{}'.format(f1, f2), end='-')
while cont <= n:
    f3 = f1 + f2
    print('{}'.format(f3), end='-')
    f1 = f2
    f2 = f3
    cont += 1
print('FIM')


