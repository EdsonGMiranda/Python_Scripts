# Exercício Python 32: Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

ano = int(input('Entre com um ano para saber se ele é bissexto ou não: '))
if (ano % 4 == 0) and (ano % 100 != 0) or (ano % 400 == 0):
     print('O ano de {} é bissexto'.format(ano))
else:
    print('O ano de {} não é bissexto.'.format(ano))
