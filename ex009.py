# Exercício Python 9: Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada.

n = int(input('Entre com um  número : '))
for i in range(11):
    print('{} x {} = {}'.format(n, i, (n * i)))
