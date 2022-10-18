# Exercício Python 16: Crie um programa que leia um número Real qualquer pelo teclado
# e mostre na tela a sua porção Inteira.

from math import trunc
n = float(input('Insira um numero :'))
print('O numero inserido foi {} e a sua porção inteira é {}' .format(n, trunc(n)))