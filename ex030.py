# Exercício Python 30: Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

n = int(input('Digite um numero para saber se ele é par ou impar: '))
if n % 2 == 0:
    print('O numero {} é par'.format(n))
else:
    print('O numero {} é impar'.format(n))